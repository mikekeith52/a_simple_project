-- no matter how many places within my larger query uses these dates, they can always be set here
-- the way I have it written, they are expecting values to be passed from a python script (the curly brackets play nicely with Python)
-- however, it's also easy enough to manually paste my dates in if I need to debug this query
with glbs as (
    select 
        date '{start}' as start_date
        , date '{end}' as end_date
    from dual -- dual is a special table used for setting parameters of a query
)

-- this is a pertty simple query that will get three grouped variables and one numeric variable summed up in an aggregate function
-- notice how I write the query. It is easy to see which variables are being selected. You can easily find the from, where, and group by clauses. Line breaks are used liberally
-- good coding format goes a long way!!
select col1
    , col2
    , col3
    , sum(numeric_col) as summed_numeric_col

from schema.table1 a

inner join glbs b
on a.date_col between b.start_date and b.end_date

where condition1 is not null
and condition2 = condition3

group by col1
    , col2
    , col3