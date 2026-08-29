from docx import Document

doc = Document()
doc.add_heading('Python & Backend Knowledge Summary', 0)

summary_text = """
Python Core & Data Structures
• Типизация и Модель Памяти: Мутабельные и немутабельные типы данных, мутация объектов внутри tuple, физический смысл id() в CPython и механизмы работы Pass-by-Object-Reference.
• Встроенные Коллекции: Алгоритмическая сложность (Big-O) операций в list, dict, set, tuple, превосходство метода .join() над конкатенацией через +.
• Функциональные Механизмы: Сигнатуры функций (*args, **kwargs, positional/keyword-only), область видимости (правило LEGB), замыкания (closures).
• Итерация и Протоколы: Итераторы и генераторы (yield), выразительность list / set / dict / generator comprehensions.
• Продвинутый Функционал: Декораторы (включая параметризованные и на классах), контекстные менеджеры (with, протокол __enter__ / __exit__).

ООП, Архитектура & Паттерны
• Базовое ООП: Инкапсуляция, наследование, полиморфизм, dunder-методы (__init__, __str__, __call__ и др.).
• Множественное Наследование: Порядок разрешения методов (MRO, алгоритм C3-linearization).
• Архитектурные Принципы: SOLID, DRY, KISS, YAGNI, расчет и снижение цикломатической сложности (Cyclomatic Complexity).
• Паттерны Проектирования: Abstract Factory, Decorator и другие порождающие/структурные паттерны.

CPython Internals & Concurrency
• Управление Памятью: Устройство Stack/Heap, аллокатор PyMalloc, сборщик мусора (GC) с подсчетом ссылок (Reference Counting) и тремя поколениями (Generations 0-2) для циклических ссылок.
• Параллелизм и Конкурентность:
  - Threading (потоки ОС, GIL, задачи с упором на I/O-bound).
  - Multiprocessing (изолированные процессы для CPU-bound задач).
  - Asyncio (кооперативная многозадачность, Event Loop, Coroutines, Tasks, Futures).

Базы Данных & ORM (SQL / SQLAlchemy)
• Фундамент Реляционных СУБД: Транзакции и гарантии ACID, уровни изоляции (Read Uncommitted -> Serializable) и предотвращение аномалий.
• Индексация и Соединения: Устройство B-Tree и Hash индексов, правило левого префикса, типы JOIN (INNER, LEFT, FULL) и алгоритмы их выполнения (Nested Loop, Hash Join, Merge Join).
• ORM & Паттерны БД: Работа с SQLAlchemy 2.0 (Core и ORM), проблема N+1 и методы её решения (joinedload, selectinload), паттерны Unit of Work, Repository, Identity Map, Active Record vs Data Mapper.
• Жизненный Цикл Объектов: Состояния Transient, Pending, Persistent, Dirty, Detached.

Сети & Web Development
• Сетевой Стек: Основы стек-протоколов TCP/IP, IP-адресация.
• Web-Протоколы: Устройство HTTP/HTTPS (запросы, ответы, заголовки, статус-коды).
• Архитектура API: Принципы REST API, идемпотентность методов (GET, PUT, DELETE vs POST), разница между PUT и PATCH.
"""

for line in summary_text.strip().split('\n'):
    if line.strip() and not line.startswith('•') and not line.startswith('  -'):
        doc.add_heading(line.strip(), level=1)
    elif line.strip():
        doc.add_paragraph(line.strip())

doc.save('python_interview_summary.docx')
print("Файл python_interview_summary.docx успешно создан!")