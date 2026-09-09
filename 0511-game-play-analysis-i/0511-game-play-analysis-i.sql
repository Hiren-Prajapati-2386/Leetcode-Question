# Write your MySQL query statement below


with newTabel as(
select player_id,event_date,
        dense_rank() over(partition by player_id order by event_date) as rn
        from Activity)

select player_id,event_date as first_login from newTabel
where rn = 1