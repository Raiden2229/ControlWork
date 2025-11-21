import flet as ft

class Item:
    def__init__(self, name, bought=False)
    self.name = name
    self.bought = bought


def main(page: ft.Page):
    items = []

    new_item_input = ft.TextField(label="введите товар", autofocus=True)
    items_list = ft.Column()
    add_button = ft.ElevatedButton("ADD", on_click=lambda e: add_item())
    sort_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("все"),
            ft.dropdown.Option("купленные"),
            ft.dropdown.Option("некупленные"),
        ],
        label = "фильтр",
        on_change=lambda e: update_list()
    )

    def add_item():
        item_name = new_item_input.value.strip()
        if item_name:
            items.append(Item(item_name))
            new_item_input.value = ""
            update_list()
            page.update()

    def update_list():
        filtered_items = []
        filter_option = sort_dropdown.value
        if filter_option == "все":
            filtered_items = items
        elif filter_option == "купленные":
            filtered_items = [item for item in items if item.bought]
        elif filter_option == "некупленные":
            filtered_items = [ item for item in items if not item.bought]

        items_list.controls.clear()
        for item in filtered_items:
            items_list.controls.append(
                ft.Row(
                    [ 
                        ft.Checkbox(
                            label=item_name,
                            value=item.bought,
                            on_change=lambda e, i=item: toggle_bought(i)
                        ),
                        ft.IconButton(
                            ft.icons.DELETE,
                            on_click=lambda e, i=item: delete_item(i),
                            icon_size=20
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START
                )
            )
            page.update()

    def toggle_bought(item: Item):
        item.bought = not item.bought
        update_list()

    def delete_item(item:Item):
        items.remove(item)
        update_list()

    page.add(
        ft.Column(
            [
                ft.Text("список покупок", size=24),
                new_item_input,
                add_button,
                sort_dropdown,
                items_list

            ]
        )
    )

    ft.app(target=main)