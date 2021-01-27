### mysql学习


#  创建表
create table user(id int ,primary key(id));

#  查询表
select * from  user  limit  3,5;   
limit 按照行数查

#  修改字段
alter table user add name varchar(20);

#  修改表的名称
alter tabel user rename to userNewname;

#  修改表注释 
alter table sys_application comment '系统信息表';

#  修改字段类型和注释
alter table sys_application  modify column app_name varchar(20) COMMENT '应用的名称';

#  增加主键 
alter table t_app add aid int(5) not null ,add primary key (aid);  