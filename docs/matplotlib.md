# Заметки - справочник функций библиотеки Matplotlib

## Импорт и настройка

- `import matplotlib.pyplot as plt` - стандартный импорт pyplot;
- `plt.style.use('seaborn-v0_8')` - применение стиля оформления;
- `plt.rcParams['figure.figsize'] = (10, 6)` - глобальная настройка размера фигур;
- `plt.rcParams['font.size'] = 12` - глобальная настройка размера шрифта;

## Создание фигур и осей

- `plt.figure()` - создание новой фигуры;
- `plt.figure(figsize=(10, 6))` - фигура с заданным размером (дюймы);
- `plt.subplots()` - создание фигуры и осей (возвращает (fig, ax));
- `plt.subplots(nrows=2, ncols=2)` - сетка 2x2 подграфиков;
- `plt.subplot(2, 2, 1)` - создание подграфика в сетке (2x2, позиция 1);
- `fig.add_subplot(111)` - добавление осей на фигуру;

## Базовые графики

- `plt.plot(x, y)` - линейный график;
- `plt.plot(x, y, 'ro-')` - линейный график со стилем (красные точки-кружки, линия);
- `plt.scatter(x, y)` - точечная диаграмма (скаттер);
- `plt.bar(x, height)` - столбчатая диаграмма;
- `plt.barh(y, width)` - горизонтальная столбчатая диаграмма;
- `plt.hist(data, bins=30)` - гистограмма;
- `plt.pie(sizes, labels=labels)` - круговая диаграмма;
- `plt.boxplot(data)` - ящик с усами (boxplot);
- `plt.stem(x, y)` - стеблевой график;
- `plt.step(x, y)` - ступенчатый график;
- `plt.fill_between(x, y1, y2)` - заполнение области между кривыми;

## Настройка стилей линий и маркеров

- `'r'` - красный цвет (red);
- `'b'` - синий (blue);
- `'g'` - зеленый (green);
- `'k'` - черный (black);
- `'--'` - пунктирная линия;
- `'-.'` - штрих-пунктирная линия;
- `':'` - точечная линия;
- `'o'` - кружок в маркере;
- `'s'` - квадрат;
- `'^'` - треугольник вверх;
- `'v'` - треугольник вниз;
- `'+'` - плюс;
- `'x'` - крест (икс);

## Параметры plot

- `linewidth=2` - толщина линии (или lw);
- `markersize=5` - размер маркера (или ms);
- `markerfacecolor='red'` - цвет заливки маркера (или mfc);
- `markeredgecolor='black'` - цвет границы маркера (или mec);
- `alpha=0.7` - прозрачность (0 - прозрачный, 1 - непрозрачный);
- `label='Подпись'` - метка для легенды;
- `linestyle='dashed'` - стиль линии (или ls);

## Оси и подписи

- `plt.xlabel('X label')` - подпись оси X;
- `plt.ylabel('Y label')` - подпись оси Y;
- `plt.title('Title')` - заголовок графика;
- `plt.suptitle('Main Title')` - общий заголовок для всей фигуры;
- `plt.xlim(0, 10)` - границы оси X;
- `plt.ylim(0, 100)` - границы оси Y;
- `plt.xticks([0, 1, 2, 3])` - установка меток на оси X;
- `plt.xticks([0, 1, 2, 3], ['A', 'B', 'C', 'D'])` - метки с подписями;
- `plt.xticks(rotation=45)` - поворот меток на 45 градусов;
- `plt.grid(True)` - включение сетки;
- `plt.grid(axis='y', linestyle='--', alpha=0.7)` - сетка только по Y с настройками;

## Легенда

- `plt.legend()` - отображение легенды (использует label из plot);
- `plt.legend(loc='upper right')` - позиция легенды;
- `plt.legend(bbox_to_anchor=(1.05, 1))` - позиция за пределами графика;
- `plt.legend(fontsize=10)` - размер шрифта легенды;
- `plt.legend(frameon=False)` - убрать рамку легенды;
- `plt.legend(ncol=2)` - легенда в 2 колонки;

## Множественные графики

- `plt.plot(x1, y1, label='Line 1')` - первый график;
- `plt.plot(x2, y2, label='Line 2')` - второй график (на тех же осях);
- `plt.twinx()` - создание второй оси Y (разные масштабы);
- `plt.twiny()` - создание второй оси X;

## Работа с осями (объектно-ориентированный стиль)

- `fig, ax = plt.subplots()` - создание фигуры и осей;
- `ax.plot(x, y)` - линейный график на осях;
- `ax.set_xlabel('X')` - подпись оси X;
- `ax.set_ylabel('Y')` - подпись оси Y;
- `ax.set_title('Title')` - заголовок;
- `ax.set_xlim(0, 10)` - границы оси X;
- `ax.legend()` - легенда;
- `ax.grid(True)` - сетка;
- `ax.axhline(y=0, color='k', linestyle='-')` - горизонтальная линия;
- `ax.axvline(x=0, color='k', linestyle='-')` - вертикальная линия;
- `ax.axvspan(xmin, xmax, alpha=0.3)` - вертикальная заливка области;

## Текст и аннотации

- `plt.text(x, y, 'text')` - добавление текста на график;
- `plt.annotate('point', xy=(x, y), xytext=(x+1, y+1), arrowprops=dict(arrowstyle='->'))` - аннотация со стрелкой;
- `plt.figtext(0.5, 0.95, 'Figure Text')` - текст на уровне фигуры;
- `plt.suptitle('Title', y=0.95)` - общий заголовок с позицией;

## Цветовые карты (colormaps)

- `plt.cm.viridis` - колормеп viridis;
- `plt.cm.plasma` - колормеп plasma;
- `plt.cm.RdBu` - красно-синяя колормеп;
- `plt.cm.Set1` - дискретная колормеп;
- `scatter = plt.scatter(x, y, c=values, cmap='viridis')` - использование colormap;
- `plt.colorbar(scatter)` - добавление цветовой шкалы;
- `plt.colorbar(label='Value')` - цветовая шкала с подписью;

## Специализированные графики

- `plt.contour(X, Y, Z)` - контурный график;
- `plt.contourf(X, Y, Z)` - залитый контурный график;
- `plt.imshow(matrix, cmap='hot')` - отображение матрицы как изображения;
- `plt.pcolormesh(X, Y, Z)` - сеточный график с цветом;
- `plt.quiver(X, Y, U, V)` - векторное поле;
- `plt.streamplot(X, Y, U, V)` - линии тока;
- `plt.semilogx(x, y)` - логарифмическая ось X;
- `plt.semilogy(x, y)` - логарифмическая ось Y;
- `plt.loglog(x, y)` - обе оси логарифмические;
- `plt.errorbar(x, y, yerr=err)` - график с погрешностями;

## 3D графики

- `from mpl_toolkits.mplot3d import Axes3D` - импорт для 3D;
- `fig = plt.figure(); ax = fig.add_subplot(111, projection='3d')` - создание 3D осей;
- `ax.plot3D(x, y, z)` - 3D линейный график;
- `ax.scatter3D(x, y, z)` - 3D точечный график;
- `ax.plot_surface(X, Y, Z, cmap='viridis')` - 3D поверхность;
- `ax.plot_wireframe(X, Y, Z)` - каркасная поверхность;
- `ax.contour3D(X, Y, Z, 50, cmap='binary')` - 3D контуры;
- `ax.view_init(elev=30, azim=45)` - угол обзора;

## Сохранение графиков

- `plt.savefig('plot.png')` - сохранение в PNG;
- `plt.savefig('plot.pdf')` - сохранение в PDF;
- `plt.savefig('plot.svg')` - сохранение в SVG;
- `plt.savefig('plot.jpg', dpi=300)` - с высоким разрешением;
- `plt.savefig('plot.png', bbox_inches='tight')` - обрезка лишних полей;
- `plt.savefig('plot.png', transparent=True)` - прозрачный фон;

## Управление отображением

- `plt.show()` - отображение графика (в скриптах);
- `plt.close()` - закрыть текущую фигуру;
- `plt.close('all')` - закрыть все фигуры;
- `plt.clf()` - очистить текущую фигуру;
- `plt.cla()` - очистить текущие оси;
- `fig.clf()` - очистить фигуру;
- `fig.savefig('file.png')` - сохранение из объекта фигуры;

## Работа с датами

- `from matplotlib.dates import DateFormatter, DayLocator` - импорт для дат;
- `plt.plot_date(dates, values)` - график с датами;
- `ax.xaxis.set_major_locator(DayLocator())` - основные деления по дням;
- `ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))` - формат дат;
- `fig.autofmt_xdate()` - автоматический поворот подписей дат;

## Анимация

- `from matplotlib.animation import FuncAnimation` - импорт для анимации;
- `anim = FuncAnimation(fig, update_func, frames=100, interval=50)` - создание анимации;
- `anim.save('animation.gif', writer='pillow')` - сохранение анимации;
- `plt.pause(0.01)` - пауза для обновления в реальном времени (интерактивные графики);

## Работа с осями (продвинутые настройки)

- `ax.spines['top'].set_visible(False)` - скрыть верхнюю рамку;
- `ax.spines['right'].set_visible(False)` - скрыть правую рамку;
- `ax.xaxis.set_ticks_position('bottom')` - позиция меток оси X;
- `ax.tick_params(axis='both', which='major', labelsize=10)` - настройка параметров делений;
- `ax.set_facecolor('#f0f0f0')` - цвет фона осей;
- `fig.patch.set_facecolor('white')` - цвет фона фигуры;

## Вспомогательные функции

- `np.linspace(0, 10, 100)` - создание массива из 100 точек от 0 до 10;
- `np.arange(0, 10, 0.1)` - массив от 0 до 10 с шагом 0.1;
- `plt.tight_layout()` - автоматическое выравнивание элементов;
- `plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9)` - ручная настройка отступов;
- `plt.gcf()` - получить текущую фигуру (get current figure);
- `plt.gca()` - получить текущие оси (get current axes);
- `plt.setp(ax.get_xticklabels(), rotation=45)` - установка свойств объектов;