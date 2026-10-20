# Use cases

This document describes the first version of TaskCraft from the user's point
of view. In this version, every task is private and assigned to the user who
created it. Team tasks, reassignment, priorities, filtering, sorting, and
searching are outside the current scope.

## UC-01: Create a task

**Primary actor:** User

**Goal:** Record a new task that the user needs to complete.

**Preconditions:**

 * The user is known to the application.

**Trigger:** The user chooses to create a task.

**Main flow:**

1. The application shows fields for a title, description, and due date.
2. The user enters the task information and submits it.
3. The application validates the entered information.
4. The application creates the task, assigns it to the user, and marks it as
   not done.
5. The application confirms that the task was created.

**Alternative and error flows:**

 * If the title or due date is missing, the application explains which field
   is required and does not create the task.
 * If the due date is invalid, the application asks the user to correct it and
   does not create the task.
 * The description may be empty.

**Postconditions:**

 * The new task is stored with a unique identifier.
 * The creator and assignee both refer to the current user.
 * The task appears in the user's task overview.

## UC-02: Delete a task

**Primary actor:** User

**Goal:** Permanently remove one of the user's tasks.

**Preconditions:**

 * The task exists.
 * The task belongs to the user.

**Trigger:** The user chooses to delete a task.

**Main flow:**

1. The application asks the user to confirm the deletion.
2. The user confirms.
3. The application verifies that the task belongs to the user.
4. The application permanently deletes the task.
5. The application confirms that the task was deleted and no longer shows it
   in the overview.

**Alternative and error flows:**

 * If the user cancels the confirmation, the task remains unchanged.
 * If the task does not exist, the application reports that it could not be
   found.
 * If the task does not belong to the user, the application does not reveal or
   delete it.

**Postconditions:**

 * After a confirmed successful deletion, the task can no longer be retrieved.

## UC-03: Mark a task as done

**Primary actor:** User

**Goal:** Record that one of the user's tasks has been completed.

**Preconditions:**

 * The task exists.
 * The task belongs to the user.
 * The task is not already marked as done.

**Trigger:** The user chooses to mark a task as done.

**Main flow:**

1. The application verifies that the task belongs to the user.
2. The application marks the task as done.
3. The application shows the updated state in the overview.

**Alternative and error flows:**

 * If the task does not exist, the application reports that it could not be
   found.
 * If the task does not belong to the user, the application does not reveal or
   change it.
 * If the task is already done, it remains done and no duplicate change is
   created.

**Postconditions:**

 * The task is stored as done.
 * The task remains visible in the overview.

## UC-04: Show the task overview

**Primary actor:** User

**Goal:** See all tasks that belong to the user.

**Preconditions:**

 * The user is known to the application.

**Trigger:** The user opens the task overview.

**Main flow:**

1. The application retrieves only tasks that belong to the user.
2. The application displays each task's title, description, due date,
   assignee, and done state.
3. Open and completed tasks are both included and are visually
   distinguishable.

**Alternative and error flows:**

 * If the user has no tasks, the application shows an empty state and offers a
   way to create the first task.
 * If the tasks cannot be loaded, the application reports the problem and
   offers a way to try again.

**Postconditions:**

 * No task data is changed.
 * Tasks belonging to other users are not shown.

## Initial acceptance coverage

The first implementation should at least verify that:

 * valid task data creates a private, open task assigned to its creator;
 * missing or invalid required data does not create a task;
 * a user cannot view, complete, or delete another user's task;
 * confirming deletion removes a task and cancelling does not;
 * marking an open task as done updates its state;
 * the overview includes the user's open and completed tasks; and
 * an empty overview displays an appropriate empty state.
