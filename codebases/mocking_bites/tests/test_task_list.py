from lib.task_list import TaskList
from unittest.mock import Mock

def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour
def test_task_list_all_complete_empty():
    task_list = TaskList()
    result = task_list.all_complete()
    assert result == False

def test_task_list_all_complete_false():
    task_list = TaskList()
    fake_complete_task = Mock()
    fake_complete_task.is_complete.return_value = True
    fake_incomplete_task = Mock()
    fake_incomplete_task.is_complete.return_value = False
    task_list.add(fake_complete_task)
    task_list.add(fake_incomplete_task)
    result = task_list.all_complete()
    assert result == False

def test_task_list_all_complete_true():
    task_list = TaskList()
    fake_complete_task1 = Mock()
    fake_complete_task1.is_complete.return_value = True
    fake_complete_task2 = Mock()
    fake_complete_task2.is_complete.return_value = True
    task_list.add(fake_complete_task1)
    task_list.add(fake_complete_task2)
    result = task_list.all_complete()
    assert result == True