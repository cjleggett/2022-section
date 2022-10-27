-- Alice wants to switch from CS50 into CS51.

    -- First, do this as a multi-step process.
    SELECT id FROM people WHERE name = "Alice"; -- Alice is student 1
    SELECT id FROM courses WHERE code = "CS50"; -- CS50 is course 1
    SELECT id FROM courses WHERE code = "CS51"; -- CS51 is course 3
    UPDATE students SET course_id = 3 WHERE person_id = 1 AND course_id = 1;

    -- Then, show nested query.
    UPDATE students SET course_id = (
        SELECT id
        FROM courses
        WHERE code = "CS51"
    )
    WHERE person_id = (
        SELECT id
        FROM people
        WHERE name = "Alice"
    ) AND course_id = (
        SELECT id
        FROM courses
        WHERE code = "CS50"
    );

-- Connor Drops out :(
    DELETE FROM students
    WHERE person_id = (
        SELECT id
        FROM people
        WHERE name = "Connor"
    )

    DELETE FROM instructors
    WHERE person_id = (
        SELECT id
        FROM people
        WHERE name = "Connor"
    )

    DELETE FROM people
    WHERE name = "Connor";