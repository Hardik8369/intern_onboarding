PRAGMA foreign_keys = ON;

-- Query 1: All tasks in a specific project (Website Redesign)
SELECT t.title, t.status, t.priority, t.due_date
FROM tasks t
JOIN projects p ON t.project_id = p.id
WHERE p.name = 'Website Redesign';

-- Query 2: All pending tasks sorted by priority (highest first)
SELECT title, priority, due_date
FROM tasks
WHERE status = 'pending'
ORDER BY priority DESC;

-- Query 3: Count of tasks per project
SELECT p.name, COUNT(t.id) AS task_count
FROM projects p
LEFT JOIN tasks t ON p.id = t.project_id
GROUP BY p.id, p.name;

-- Query 4: Tasks that are overdue (pending AND due_date < '2025-01-15')
SELECT t.title, t.due_date, p.name AS project
FROM tasks t
JOIN projects p ON t.project_id = p.id
WHERE t.status = 'pending' AND t.due_date < '2025-01-15';

-- Query 5: The project with the most tasks
SELECT p.name, COUNT(t.id) AS task_count
FROM projects p
LEFT JOIN tasks t ON p.id = t.project_id
GROUP BY p.id, p.name
ORDER BY task_count DESC
LIMIT 1;
