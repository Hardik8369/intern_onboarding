PRAGMA foreign_keys = ON;

-- ============================================
-- VIEWS
-- ============================================

-- View 1: Task summary showing pending and in_progress tasks with project info
CREATE VIEW IF NOT EXISTS v_task_summary AS
SELECT 
    p.name AS project_name,
    t.title AS task_title,
    t.status,
    t.priority
FROM tasks t
JOIN projects p ON t.project_id = p.id
WHERE t.status IN ('pending', 'in_progress');

-- View 2: Project stats showing total, completed tasks and completion percentage
CREATE VIEW IF NOT EXISTS v_project_stats AS
SELECT 
    p.name AS project_name,
    COUNT(t.id) AS total_tasks,
    SUM(CASE WHEN t.status = 'completed' THEN 1 ELSE 0 END) AS completed_tasks,
    ROUND(100.0 * SUM(CASE WHEN t.status = 'completed' THEN 1 ELSE 0 END) / COUNT(t.id), 2) AS completion_percentage
FROM projects p
LEFT JOIN tasks t ON p.id = t.project_id
GROUP BY p.id, p.name;

-- ============================================
-- INDEXES
-- ============================================

-- Index on tasks.project_id for faster project-based lookups
CREATE INDEX IF NOT EXISTS idx_tasks_project_id ON tasks(project_id);

-- Index on tasks.status for faster status-based filtering
CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status);

-- ============================================
-- MULTI-TABLE JOIN (projects + tasks + task_tags)
-- ============================================

-- Join all 3 tables to show tasks with their tags
SELECT 
    p.name AS project_name,
    t.title AS task_title,
    t.status,
    tt.tag
FROM projects p
JOIN tasks t ON p.id = t.project_id
JOIN task_tags tt ON t.id = tt.task_id
ORDER BY p.name, t.title;

-- ============================================
-- WINDOW FUNCTION: Rank tasks by priority within each project
-- ============================================

-- Rank tasks by priority within each project using ROW_NUMBER()
SELECT 
    p.name AS project_name,
    t.title AS task_title,
    t.priority,
    ROW_NUMBER() OVER (PARTITION BY t.project_id ORDER BY t.priority DESC) AS priority_rank
FROM tasks t
JOIN projects p ON t.project_id = p.id;

-- ============================================
-- TRANSACTION: Add new project and tasks atomically
-- ============================================

-- Transaction to add a new project with 2 tasks atomically
BEGIN;
INSERT INTO projects (name, description) VALUES ('DevOps Setup', 'Setup CI/CD pipeline and monitoring');
INSERT INTO tasks (project_id, title, status, priority, due_date) VALUES
    ((SELECT id FROM projects WHERE name = 'DevOps Setup'), 'Setup GitHub Actions', 'pending', 4, '2025-03-01'),
    ((SELECT id FROM projects WHERE name = 'DevOps Setup'), 'Configure monitoring', 'pending', 3, '2025-03-15');
COMMIT;

-- Verify views
SELECT * FROM v_task_summary;
SELECT * FROM v_project_stats;
