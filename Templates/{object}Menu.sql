use ry;
-- 菜单 SQL
insert into sys_menu (menu_name, parent_id, order_num, url,menu_type, visible, perms, icon, create_by, create_time, update_by, update_time, remark)
values('{chinese}', '3', '1', '/system/{object}', 'C', '0', 'system:{object}:view', '#', 'admin', '2018-03-01', 'ry', '2018-03-01', '{chinese}菜单');

-- 按钮父菜单ID
SELECT @parentId := LAST_INSERT_ID();

-- 按钮 SQL
insert into sys_menu  (menu_name, parent_id, order_num, url,menu_type, visible, perms, icon, create_by, create_time, update_by, update_time, remark)
values('{chinese}查询', @parentId, '1',  '#',  'F', '0', 'system:{object}:list',         '#', 'admin', '2018-03-01', 'ry', '2018-03-01', '');

insert into sys_menu  (menu_name, parent_id, order_num, url,menu_type, visible, perms, icon, create_by, create_time, update_by, update_time, remark)
values('{chinese}新增', @parentId, '2',  '#',  'F', '0', 'system:{object}:add',          '#', 'admin', '2018-03-01', 'ry', '2018-03-01', '');

insert into sys_menu  (menu_name, parent_id, order_num, url,menu_type, visible, perms, icon, create_by, create_time, update_by, update_time, remark)
values('{chinese}修改', @parentId, '3',  '#',  'F', '0', 'system:{object}:edit',         '#', 'admin', '2018-03-01', 'ry', '2018-03-01', '');

insert into sys_menu  (menu_name, parent_id, order_num, url,menu_type, visible, perms, icon, create_by, create_time, update_by, update_time, remark)
values('{chinese}删除', @parentId, '4',  '#',  'F', '0', 'system:{object}:remove',       '#', 'admin', '2018-03-01', 'ry', '2018-03-01', '');
