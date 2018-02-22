from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
    app.group.delete_first_group()

