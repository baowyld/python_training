from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
    old_groups = app.group.get_group_list()
    group = Group(name="New group")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_modify_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(footer="New footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
