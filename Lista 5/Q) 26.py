def add_student(students: dict, name: str):
    students[name] = {}


def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return

    cursos = students[name]
    print(f"{name}:")

    if len(cursos) == 0:
        print(" no completed courses")
    else:
        print(f" {len(cursos)} completed courses:")
        for curso, nota in cursos.items():
            print(f"  {curso} {nota}")
        media = sum(cursos.values()) / len(cursos)
        print(f" average grade {media}")


def add_course(students: dict, name: str, course: tuple):
    nome_curso, nota = course

    if nota == 0:
        return

    cursos = students[name]
    if nome_curso not in cursos or nota > cursos[nome_curso]:
        cursos[nome_curso] = nota


def summary(students: dict):
    print(f"students {len(students)}")

    mais_nome = None
    mais_qtd = -1
    melhor_nome = None
    melhor_media = -1

    for nome, cursos in students.items():
        qtd = len(cursos)
        if qtd > mais_qtd:
            mais_qtd = qtd
            mais_nome = nome

        if qtd > 0:
            media = sum(cursos.values()) / qtd
            if media > melhor_media:
                melhor_media = media
                melhor_nome = nome

    print(f"most courses completed {mais_qtd} {mais_nome}")
    print(f"best average grade {melhor_media} {melhor_nome}")