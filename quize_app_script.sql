create database quize;

use quize;

drop table quiz;
drop table user_info;
create table quiz(
id int primary key not null,
quiz_question varchar(1000),
option_1 varchar(1000),
option_2 varchar(1000),
option_3 varchar(1000),
option_4 varchar(1000),
correct_ans int,
quiz_topic varchar(1000));

select * from quiz;

create table user_info(
id int primary key not null,
user_name varchar(40),
password varchar(30),
email varchar(200));


insert user_info value(1,"prabhash","veer","prabhas@hotmail.com");
select * from user_info;



