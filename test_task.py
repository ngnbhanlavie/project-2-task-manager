from main import Task, add_task, delete_task, complete_task, save, load
def test_create_task():
    task=Task(
        "Learn Python",
        1,
        "Study classes"
    )

    assert task.title=="Learn Python"
    assert task.id==1
    assert task.description=="Study classes"
    assert task.completed is False

def test_add_task(monkeypatch):
    tasks=[]

    monkeypatch.setattr(
        "builtins.input",
        lambda _:"Study classes"
    )

    add_task(tasks,"Learn Python")

    assert len(tasks)==1
    assert tasks[0].title=="Learn Python"
    assert tasks[0].description=="Study classes"
    assert tasks[0].id==1
    assert tasks[0].completed is False

def test_add_second_task(monkeypatch):
    tasks=[
        Task("First",1,"First task")
    ]

    monkeypatch.setattr(
        "builtins.input",
        lambda _:"Second task"
    )

    add_task(tasks,"Second")

    assert len(tasks)==2
    assert tasks[1].id==2

def test_delete_task():
    tasks=[
        Task("First",1,"First task"),
        Task("Second",2,"Second task")
    ]

    delete_task(tasks,1)

    assert len(tasks)==1
    assert tasks[0].id==2

def test_complete_task():
    tasks=[
        Task("Learn Python",1,"Study classes")
    ]

    complete_task(tasks,1)

    assert tasks[0].completed is True

def test_save(tmp_path, monkeypatch):
    tasks=[
        Task("Learn Python",1,"Study classes")
    ]

    monkeypatch.chdir(tmp_path)

    save(tasks)

    assert(tmp_path/"task.json").exists()

def test_save_and_load(tmp_path, monkeypatch):
    tasks=[
        Task("Learn Python",1,"Study classes"),
        Task("Learn Git",2,"Practice Git")
    ]

    monkeypatch.chdir(tmp_path)

    save(tasks)

    loaded_tasks=load()

    assert len(loaded_tasks)==2
    assert loaded_tasks[0].title=="Learn Python"
    assert loaded_tasks[0].id==1
    assert loaded_tasks[1].title=="Learn Git"
    assert loaded_tasks[1].id==2

def test_save_and_load_completed_task(tmp_path, monkeypatch):
    task = Task(
        "Learn Python",
        1,
        "Study classes"
    )

    task.complete()

    monkeypatch.chdir(tmp_path)

    save([task])

    loaded_tasks = load()

    assert loaded_tasks[0].completed is True

def test_load_without_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    tasks = load()

    assert tasks == []