select * from monthly_totals;

create table if not exists bus_monthly_totals as
select month, city, ridership_count from monthly_totals
where transportation_type='bus';

select * from bus_monthly_totals;

create table if not exists metro_monthly_totals as
select month, city, ridership_count from monthly_totals
where transportation_type='metro';

select * from metro_monthly_totals;