from random import randrange
from model.group import Group


def test_edit_group_name(app, db, check_ui):
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="new title")
    group.id = old_groups[index].id

    if len(db.get_group_list()) == 0:
        app.group.create(group)
    app.group.edit_group_by_index(index, group)

    new_groups = db.get_group_list()
    old_groups[index] = group
    assert old_groups == new_groups

    if check_ui:

        def clean(group):
            while "  " in group.name:
                group.name = group.name.replace("  ", " ")
            return Group(id=group.id, name=group.name.strip())

        db_list = map(clean, db.get_group_list())
        assert sorted(db_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_edit_group_header(app):
#     old_groups = app.group.get_group_list()
#     group = Group(header="test")
#     if app.group.count() == 0:
#         app.group.create(group)
#     app.group.edit_first_group(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


