#1) 5 студентов с наибольшим средним баллом по всем предметам.
    select last_name, avg_scores
    from students
    join (select avg(score) as avg_scores,
    student_id from scores
    group by student_id) as avm
    on students.id = avm.student_id
    order by avg_scores desc fetch first 5 row only
#2) 1 студент с наивысшим средним баллом по одному предмету.
    select group_name, subject, last_name, avg(score) from scores
    join students
    on students.id = scores.student_id
    join groups
    on groups.id = students.group_id
    where subject = 'chemistry'
    group by groups.group_name, scores.subject, students.last_name, scores.score
    order by score desc limit 1
#3) средний балл в группе по одному предмету.
    select group_name, subject, avg(score) from scores
    join students
    on students.id = scores.student_id
    join groups
    on groups.id = students.group_id
    where group_name = 'economic_121' and subject = 'chemistry'
    group by groups.group_name, scores.subject
#4) Средний балл в потоке.
    select avg(score) from scores
#5) Какие курсы читает преподаватель.
    select distinct tutor, subject from scores
    where tutor = 'Popov'
#6) Список студентов в группе.
    select group_name, first_name
    from groups, students
    where group_name = 'economic_121'
#7) Оценки студентов в группе по предмету.
    select score, group_name from scores
    join students
    on students.id = scores.student_id
    join groups
    on groups.id = students.group_id
    where group_name = 'economic_121'
#8) Оценки студентов в группе по предмету на последнем занятии.
    select group_name, score, date from scores
    join students
    on students.id = scores.student_id
    join groups
    on groups.id = students.group_id
    where group_name = 'economic_121'
    order by date desc limit 1
#9) Список курсов, которые посещает студент.
    select DISTINCT subject, last_name from scores
    join students
    on students.id = scores.student_id
    where last_name = 'Gyorgy'
#10) Список курсов, которые студенту читает преподаватель.
    select DISTINCT tutor, last_name, subject from scores
    join students
    on students.id = scores.student_id
    where last_name = 'Dare' and tutor = 'Popov'
#11) Средний балл, который преподаватель ставит студенту.
    select tutor, last_name, avg(score) from scores
    join students
    on students.id = scores.student_id
    group by tutor, students.last_name order by tutor
#12) Средний балл, который ставит преподаватель.
    select tutor, avg(score) from scores
    group by tutor order by avg(score)