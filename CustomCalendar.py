import datetime, calendar
from calendar import month

import flet
import copy

from request_file import info_calendar


class CustomCalendar(flet.Container):
    # Устанавливаем текущий месяц как текущий месяц сегодняшней даты
    _current_month = datetime.date.today().month
    # Устанавливаем текущий год как текущий год сегодняшней даты
    _current_year = datetime.date.today().year
    # Устанавливаем текущий день как текущий день сегодняшней даты
    _current_day = datetime.date.today().day
    # Получаем первый и последний день текущего месяца
    _first_day_in_month, _last_day_in_month = calendar.monthrange(
        _current_year, _current_month
    )

    _day_of_week = {0: "ПН", 1: "ВТ", 2: "СР", 3: "ЧТ", 4: "ПТ", 5: "СБ", 6: "ВС"}
    _months = {
        1: "ЯНВАРЬ",
        2: "ФЕВРАЛЬ",
        3: "МАРТ",
        4: "АПРЕЛЬ",
        5: "МАЙ",
        6: "ИЮНЬ",
        7: "ИЮЛЬ",
        8: "АВГУСТ",
        9: "СЕНТЯБРЬ",
        10: "ОКТЯБРЬ",
        11: "НОЯБРЬ",
        12: "ДЕКАБРЬ",
    }

    def __init__(
        self,
        width: int,
        bgcolor="#e2e2e2",
        font_color="#3c4457",
        font_color_accent="#ffffff",
        accent_color="#108ef2",
        header_font_color="#d2334c",
        hover_color="#eeeeee",
        border_radius=15,
    ):
        # Вызываем конструктор родительского класса
        super().__init__(
            # ширина виджета задаётся пользователем
            width=width,
            # высота считается автоматом, заголовок = width / 7, строка = width / 8
            # весь календарь это таблица 2 заголовочные строки + 5 строк на даты, ~0.5 на отступы
            height=width / 8 * 5 + width / 7 * 2.5,
            border_radius=border_radius,
            padding=flet.padding.only(0, width * 0.08, 0, 0),
            bgcolor=bgcolor,
            alignment=flet.alignment.center,
        )
        # Устанавливаем цвет шрифта
        self.font_color = font_color
        # Устанавливаем цвет шрифта для заголовка
        self.header_font_color = header_font_color
        # Устанавливаем акцентный цвет
        self.accent_color = accent_color
        # Устанавливаем цвет при наведении
        self.hover_color = hover_color
        # Устанавливаем акцентный цвет шрифта
        self.font_accent_color = font_color_accent
        # Устанавливаем размер шрифта
        self.font_size = width * 0.045
        # Рисуем базовый виджет
        self.content = self._draw_base()

    def _draw_base(self):
        # Создаем контейнер для отображения дня
        day_container = flet.Container(
            content=flet.Text(
                value="",
                text_align=flet.TextAlign.CENTER,
                weight=flet.FontWeight.W_500,
                size=self.font_size + 2,
                color=self.font_color,
            ),
            width=(self.width - self.width * 0.05) / 8,
            height=self.width / 8,
            alignment=flet.alignment.center,
            shape=flet.BoxShape.CIRCLE,
            on_hover=self._on_hover_date,
            data="",
        )
        # Создаем базовый виджет календаря
        custom_calendar = flet.Column(
            controls=[
                # Создаем строку с кнопками для перелистывания календаря и названием месяца и года
                flet.Row(
                    controls=[
                        flet.Container(
                            flet.IconButton(
                                icon=flet.icons.KEYBOARD_ARROW_LEFT_SHARP,
                                height=self.width / 11,
                                width=self.width / 7,
                                icon_size=self.font_size,
                                padding=0,
                                icon_color=self.font_color,
                                data="left_flip",
                                on_click=self._flip_calendar,
                            ),
                            height=self.width / 8,
                            alignment=flet.alignment.center,
                        ),
                        flet.Container(
                            flet.Text(
                                value="",
                                spans=[
                                    flet.TextSpan(
                                        "", flet.TextStyle(weight=flet.FontWeight.BOLD)
                                    )
                                ],
                                weight=flet.FontWeight.W_400,
                                color=self.font_color,
                                size=self.font_size + 2,
                                text_align=flet.alignment.center,
                            ),
                            height=self.width / 8,
                            alignment=flet.alignment.center,
                        ),
                        flet.Container(
                            flet.IconButton(
                                icon=flet.icons.KEYBOARD_ARROW_RIGHT_SHARP,
                                icon_size=self.font_size,
                                height=self.width / 10,
                                width=self.width / 7,
                                padding=0,
                                data="right_flip",
                                on_click=self._flip_calendar,
                                icon_color=self.font_color,
                            ),
                            height=self.width / 8,
                            alignment=flet.alignment.center,
                        ),
                    ],
                    alignment=flet.MainAxisAlignment.CENTER,
                    vertical_alignment=flet.CrossAxisAlignment.START,
                ),
                # Создаем строку с днями недели
                flet.Row(
                    controls=[
                        flet.Text(
                            value=self._day_of_week.get(i),
                            text_align=flet.TextAlign.CENTER,
                            width=(self.width - self.width * 0.08) / 7.8,
                            weight=flet.FontWeight.W_400,
                            size=self.font_size,
                            color=self.header_font_color,
                            height=self.width / 8,
                        )
                        for i in range(0, 7)
                    ],
                    alignment=flet.MainAxisAlignment.CENTER,
                    height=self.width / 10,
                    spacing=0,
                ),
                # Создаем пять строк на даты
                *[
                    flet.Row(
                        controls=[copy.deepcopy(day_container) for i in range(0, 7)],
                        alignment=flet.MainAxisAlignment.CENTER,
                        spacing=0,
                    )
                    for i in range(0, 5)
                ],
            ],
            spacing=0,
        )
        # Заполняем даты в календаре
        self._fill_dates(custom_calendar)
        # Возвращаем базовый виджет календаря
        return custom_calendar

    def _fill_dates(self, custom_calendar):
        # Устанавливаем счетчик дней на 1
        day_counter = 1
        # Получаем первый и последний день текущего месяца
        self._first_day_in_month, self._last_day_in_month = calendar.monthrange(
            self._current_year, self._current_month
        )
        # Устанавливаем значение текста в заголовке календаря на название текущего месяца и год
        custom_calendar.controls[0].controls[1].content.value = self._months.get(
            self._current_month
        )
        custom_calendar.controls[0].controls[1].content.spans[0].text = " " + str(
            self._current_year
        )
        # Проходим по каждой строке в календаре
        for row_id, row in enumerate(custom_calendar.controls):
            # Пропускаем первые две строки, так как они являются заголовками календаря
            if row_id < 2:
                continue
            # Проходим по каждому столбцу в строке
            for column_id, column in enumerate(row.controls):

                # Если текущий день меньше первого дня месяца, устанавливаем значение текста в столбце на "ꟷ"
                if row_id - 2 == 0 and column_id < self._first_day_in_month:
                    column.content.value = "ꟷ"
                    column.content.weight = flet.FontWeight.W_200
                # Если счетчик дней меньше или равен последнему дню месяца, устанавливаем значение текста в столбце на текущий день
                elif self._last_day_in_month >= day_counter:
                    column.content.value = str(day_counter)
                    column.content.weight = flet.FontWeight.W_500
                    # Если текущий день равен текущему дню, месяцу и году, устанавливаем цвет фона и шрифта на акцентные цвета
                    if (
                        day_counter == self._current_day
                        and self._current_month == CustomCalendar._current_month
                        and self._current_year == CustomCalendar._current_year
                    ):

                        column.bgcolor = self.accent_color
                        column.content.color = self.font_accent_color
                        column.data = "today"
                    # В противном случае устанавливаем цвет фона и шрифта на обычные цвета
                    else:
                        column.bgcolor = self.bgcolor
                        column.content.color = self.font_color
                        column.data = "just_a_day"

#________________-цвет даты___________________--------------------------------------
                    list_calendar = [i['date_training'] for i in info_calendar()]
                    for cal in list_calendar:
                        list_year = cal[:cal.find('-')]
                        list_day = cal[cal.rfind('-')+1:]
                        list_month = cal[cal.find('-')+1:cal.rfind('-')]
                        if list_day[0] == '0' or list_month[0] == '0':
                            list_day = list_day[1:]
                            list_month = list_month[1:]
                        if (day_counter == int(list_day)
                        and self._current_month == int(list_month)
                        and self._current_year == int(list_year)):
                            column.bgcolor = 'yellow'
                            column.content.color = 'black'
                            column.data = "event"
#-----------------------------------------------------------------------------------

                    # Увеличиваем счетчик дней на 1
                    day_counter += 1
                # Если счетчик дней больше последнего дня месяца, устанавливаем значение текста в столбце на "ꟷ"
                else:
                    column.content.value = "ꟷ"
                    column.content.weight = flet.FontWeight.W_200

    def _on_hover_date(self, e: flet.ControlEvent):
        # Когда мышь на элементе e.data = "true"
        e.control.bgcolor = (
            self.hover_color
            if e.data == "true" and e.control.data != "today"
            else (self.accent_color if e.control.data == "today" else self.bgcolor)
        )
        e.control.update()

    def _flip_calendar(self, e: flet.ControlEvent):
        # Проверяем, была ли нажата кнопка "left_flip"
        if e.control.data == "left_flip":
            # Если текущий месяц больше 1, уменьшаем его на 1
            if self._current_month - 1 > 0:
                self._current_month = self._current_month - 1
            # Если текущий месяц равен 1, устанавливаем его в 12 и уменьшаем год на 1
            else:
                self._current_month = 12
                self._current_year = self._current_year - 1
        # Проверяем, была ли нажата кнопка "right_flip"
        elif e.control.data == "right_flip":
            # Если текущий месяц меньше 12, увеличиваем его на 1
            if self._current_month + 1 < 12:
                self._current_month = self._current_month + 1
            # Если текущий месяц равен 12, устанавливаем его в 1 и увеличиваем год на 1
            else:
                self._current_month = 1
                self._current_year = self._current_year + 1
        # Заполняем даты в календаре
        self._fill_dates(self.content)
        # Обновляем содержимое календаря
        self.content.update()


def main_page(page: flet.Page):
    page.title = "Custom Calendar Widget"
    my_calendar3 = CustomCalendar(
        width=250,
        bgcolor="#71a95a",
        font_color="#ffffff",
        hover_color="#34d409",
        font_color_accent="#84ff17",
        accent_color="#d2334c",
        header_font_color="#ffffff",
    )

    my_row = flet.Row(controls=[my_calendar3], wrap=True)
    page.add(my_row)


if __name__ == "__main__":
    flet.app(target=main_page)
