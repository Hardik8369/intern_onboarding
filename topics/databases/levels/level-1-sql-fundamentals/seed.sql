PRAGMA foreign_keys = ON;

-- Insert projects
INSERT INTO projects (name, description) VALUES
('Website Redesign', 'Redesign the company website with modern UI'),
('Mobile App', 'Build a mobile app for iOS and Android'),
('Data Pipeline', 'Build an automated data processing pipeline');

-- Insert tasks
INSERT INTO tasks (project_id, title, status, priority, due_date) VALUES
(1, 'Design homepage mockup', 'completed', 5, '2025-01-10'),
(1, 'Implement navbar', 'in_progress', 4, '2025-02-01'),
(1, 'Fix login page bug', 'pending', 5, '2025-01-10'),
(1, 'Write CSS for footer', 'pending', 2, '2025-03-01'),
(2, 'Setup React Native', 'completed', 5, '2025-01-05'),
(2, 'Build login screen', 'in_progress', 4, '2025-02-15'),
(2, 'Integrate API', 'pending', 3, '2025-01-12'),
(2, 'Write unit tests', 'pending', 2, '2025-03-10'),
(3, 'Setup ETL pipeline', 'in_progress', 5, '2025-02-01'),
(3, 'Write data validation', 'pending', 3, '2025-01-08'),
(3, 'Deploy to production', 'pending', 4, '2025-04-01');

-- Insert task tags
INSERT INTO task_tags (task_id, tag) VALUES
(1, 'frontend'),
(2, 'frontend'),
(3, 'urgent'),
(4, 'frontend'),
(5, 'backend'),
(6, 'frontend'),
(7, 'backend'),
(8, 'testing'),
(9, 'backend'),
(10, 'urgent');
