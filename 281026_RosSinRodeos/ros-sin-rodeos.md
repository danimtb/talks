---
marp: true
lang: es
theme: default
size: 16:9
paginate: true
title: "ROS sin rodeos: Desarrollo nativo en C++ para robótica"
description: "ROSCon España 2026 · Valencia · 28 de octubre de 2026"
author: "Daniel Manzaneque · Ingeniero Software en Conan / JFrog"
footer: "**ROS sin rodeos** · Daniel Manzaneque [![Conan](img/conan-cube.png) `conan.io`](https://conan.io) [`github.com/conan-io/ros-conan`](https://github.com/conan-io/ros-conan)"
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

  /* Paleta y tipografía tomadas de conan.io */
  :root {
    --ink: #0b1220;
    --ink-2: #2a3346;
    --ink-3: #5b657a;
    --line: #e6eaf2;
    --line-2: #d7deec;
    --soft: #f4f7fc;
    --blue: #1a73e8;
    --blue-deep: #0e4fb8;
    --blue-ink: #082b6b;
    --blue-soft: #e6f0fe;
    --blue-ultra: #f3f7fe;
    --frog: #6fb752;
    --frog-dark: #3e7a2d;
    --green-soft: #dbf4e5;
    --green-ink: #0e5a35;
    --red-soft: #fdecec;
    --red-ink: #a11a1a;
    --sans: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;
    --mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  }

  section {
    font-family: var(--sans);
    font-size: 29px;
    line-height: 1.45;
    color: var(--ink-2);
    background: linear-gradient(180deg, var(--blue-ultra) 0%, #ffffff 38%);
    padding: 78px 80px 64px 80px;
  }

  h1, h2 { color: var(--blue-ink); font-weight: 800; letter-spacing: -0.03em; line-height: 1.1; }
  h1 { font-size: 2.3em; }
  h2 { font-size: 1.45em; margin: 0 0 0.6em 0; }
  h1 em, h2 em { font-style: normal; color: var(--blue); }
  strong { color: var(--ink); font-weight: 700; }
  a { color: var(--blue); }

  /* Etiqueta de sección: la "pill" monoespaciada de conan.io */
  h6 {
    display: inline-block; margin: 0 0 .7em 0; padding: .3em .7em;
    font-family: var(--mono); font-size: 0.52em; font-weight: 500;
    letter-spacing: .02em; text-transform: none;
    color: var(--blue-deep); background: var(--blue-soft);
  }
  h6 code { background: transparent; padding: 0; color: inherit; font-size: 1em; }

  ul, ol { margin-top: .2em; }
  li { margin: .3em 0; }
  li::marker { color: var(--blue); }

  code {
    font-family: var(--mono); font-size: .86em;
    background: var(--blue-soft); color: var(--blue-ink);
    padding: .08em .35em; border-radius: 0;
  }
  pre {
    background: var(--soft); border: 1px solid var(--line); border-left: 4px solid var(--blue);
    border-radius: 0; font-size: 0.66em; line-height: 1.5; padding: .75em 1em; margin: .3em 0 .8em 0;
  }
  pre code { background: transparent; padding: 0; font-size: 1em; color: var(--ink); }

  blockquote {
    border-left: 4px solid var(--frog); background: var(--soft); color: var(--ink-2);
    padding: .5em .9em; margin: .8em 0 0 0; font-size: .82em; font-style: normal;
  }

  table { font-size: .8em; border-collapse: collapse; width: 100%; display: table; }
  th { background: var(--blue-ink); color: #fff; text-align: left; font-weight: 600; }
  td, th { padding: .55em .8em; border: 1px solid var(--line-2); }
  tr:nth-child(even) td { background: var(--soft); }
  td:first-child { white-space: nowrap; font-weight: 600; color: var(--blue-ink); }

  /* Cabecera con el logo JFrog · Conan y pie */
  header { left: auto; right: 48px; top: 26px; }
  header img { height: 34px; }
  /* Pie permanente con las referencias a Conan: discreto pero siempre visible */
  footer {
    left: 80px; right: 80px; bottom: 18px; padding-top: 10px;
    border-top: 1px solid var(--line);
    font-family: var(--mono); font-size: 16px; color: var(--ink-3);
    display: flex; align-items: center; gap: 22px;
  }
  footer { padding-right: 56px; }
  footer { white-space: nowrap; }
  /* Izquierda: título de la charla y ponente. Derecha: referencias a Conan */
  footer strong {
    font-family: var(--sans); font-weight: 700; color: var(--blue-ink);
    letter-spacing: -0.01em; margin-right: -14px;
  }
  footer > a:first-of-type { margin-left: auto; }
  footer a {
    display: inline-flex; align-items: center; gap: 8px;
    color: var(--ink-3); text-decoration: none;
  }
  footer a code { background: transparent; color: inherit; padding: 0; font-size: 1em; }
  footer img { height: 17px; width: auto; }
  footer a:last-of-type::before {
    content: ""; width: 16px; height: 16px; flex: none;
    background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath fill='%235b657a' d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/%3E%3C/svg%3E") no-repeat center / contain;
  }
  section::after { font-size: 15px; color: var(--ink-3); font-family: var(--mono); right: 80px; bottom: 17px; padding: 0; }

  /* Portada: como el hero de conan.io */
  section.hero { justify-content: center; padding-right: 40px; }
  section.hero h1 { font-size: 2.9em; margin: 0 0 .25em 0; }
  section.hero h2 { color: var(--ink-2); font-weight: 500; font-size: 1.05em; letter-spacing: 0; margin-bottom: 1.4em; }
  section.hero p { font-size: .85em; margin: .15em 0; }

  /* Bloques oscuros: como la sección azul de conan.io */
  section.dark {
    background:
      radial-gradient(circle at 88% 16%, rgba(26,115,232,.60) 0, rgba(26,115,232,0) 32%),
      var(--blue-ink);
    color: #c9d3e6; justify-content: center;
  }
  section.dark h1, section.dark h2, section.dark strong { color: #ffffff; }
  section.dark h1 em, section.dark h2 em { color: #6aa8ff; }
  section.dark h6 { background: rgba(255,255,255,.10); color: #c9d3e6; }
  section.dark code { background: rgba(255,255,255,.10); color: #ffffff; }
  section.dark footer, section.dark footer a, section.dark::after { color: #c9d3e6; }
  section.dark footer { border-top-color: rgba(255,255,255,.18); }
  section.dark footer strong { color: #ffffff; }
  section.dark footer code { background: transparent; color: inherit; }
  section.dark footer a:last-of-type::before { background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath fill='%23c9d3e6' d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z'/%3E%3C/svg%3E"); }

  /* El rodeo (problema) y sin rodeos (solución): cambia el color de la pill */
  section.problema h6 { background: var(--red-soft); color: var(--red-ink); }
  section.solucion h6 { background: var(--green-soft); color: var(--green-ink); }
  section.solucion h2 em { color: var(--frog-dark); }

  /* Tarjetas numeradas 01 / 02 / 03, como "Why Conan" */
  section.cards ol {
    list-style: none; counter-reset: card; padding: 0; margin-top: .6em;
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px;
  }
  section.cards ol > li {
    counter-increment: card; margin: 0; background: #fff;
    border: 1px solid var(--line); padding: 1em 1em 1.1em 1em; font-size: .78em; line-height: 1.45;
  }
  section.cards ol > li::before {
    content: "0" counter(card); display: inline-block; margin-bottom: .7em;
    font-family: var(--mono); font-size: .85em; color: var(--blue-deep);
    background: var(--blue-soft); padding: .25em .55em;
  }
  section.cards ol > li strong:first-child { display: block; font-size: 1.15em; color: var(--blue-ink); margin-bottom: .35em; }

  /* Enlace grande al repo, para apuntarlo desde la sala */
  section.repo p {
    margin: 0.75em 0 0 0;
    font-family: var(--mono);
    font-size: 1.45em;
    font-weight: 600;
    line-height: 1.3;
    letter-spacing: -0.03em;
  }
  section.repo p a {
    color: var(--blue-ink);
    text-decoration: none;
    border-bottom: 4px solid var(--blue);
  }

  /* Esquema de dependencias: el grafo que no cierra */
  section.grafo h2 { margin-bottom: 0.28em; }
  section.grafo p { margin: 0.15em 0 0.05em; font-size: 0.92em; }
  section.grafo ul { margin: 0.12em 0 0; font-size: 0.84em; }
  section.grafo li { margin: 0.1em 0; }

  /* El nombre de fichero es una pastilla h6 pegada al bloque de debajo */
  h6:has(+ pre) {
    margin-bottom: 0;
    background: var(--blue-soft);
    color: var(--blue-deep);
  }
  h6 + pre { margin-top: 0; }

  /* Mascotas. --mascota-right es el hueco hasta el borde: súbelo para moverlas a la izquierda.
     El tamaño resta ese hueco: si no, el desplazamiento recorta la imagen por la izquierda. */
  section.mascota { --mascota-right: 138px; }
  section.mascota [data-marpit-advanced-background-container] figure {
    background-position: right var(--mascota-right) center !important;
    background-size: calc(100% - var(--mascota-right)) auto !important;
    background-repeat: no-repeat !important;
  }

  /* Mascota de ros2. --tools-gap la separa del borde: súbelo para traerla hacia el centro. */
  section.tools {
    --tools-gap: 150px;
    background-image: url("img/frog_turtlebot2.png"), linear-gradient(180deg, var(--blue-ultra) 0%, #ffffff 38%);
    background-repeat: no-repeat, no-repeat;
    background-position: right var(--tools-gap) center, 0 0;
    background-size: auto 68%, auto;
    padding-right: 42%;
  }

  /* Logo al presentar Conan. El PNG es ancho: cubo y wordmark, con margen transparente. */
  section.herramienta {
    background-image: url("img/conan-cube.png"), linear-gradient(180deg, var(--blue-ultra) 0%, #ffffff 38%);
    background-repeat: no-repeat, no-repeat;
    background-position: right 48px center, 0 0;
    background-size: 300px auto, auto;
    padding-right: 340px;
    font-size: 26px;
  }
  section.herramienta h2 { font-size: 1.22em; margin-bottom: 0.28em; }
  section.herramienta h4 { font-size: 1.05em; margin: 0.22em 0 0; }
  section.herramienta ul { margin: 0 0 0.08em; }
  section.herramienta li { margin: 0.06em 0; }

  /* Perfil, comando y contextos caben en una sola diapositiva */
  section.cruzado { font-size: 26px; }
  section.cruzado h2 { margin-bottom: 0.4em; }

  /* La captura va a la derecha, pero el pie sigue a todo el ancho, por debajo. */
  section.pose {
    --pose-gap: 52px;
    background-image: url("img/pose-estimation.png"), linear-gradient(180deg, var(--blue-ultra) 0%, #ffffff 38%);
    background-repeat: no-repeat, no-repeat;
    background-position: right var(--pose-gap) center, 0 0;
    background-size: 46% auto, auto;
    padding-right: 44%;
  }

  /* GIF del robot centrado, con el pie de foto debajo */
  section.video h2 { margin-bottom: 0.3em; }
  section.video p { font-size: .72em; color: var(--ink-3); margin: .4em 0 0 0; text-align: center; }
  section.video p:has(img) { margin: 0; }
  section.video p img { border: 1px solid var(--line); }
---

<!-- _class: hero mascota -->
<!-- _footer: "[![Conan](img/conan-cube.png) `conan.io`](https://conan.io) [`github.com/conan-io/ros-conan`](https://github.com/conan-io/ros-conan)" -->
<!-- _paginate: false -->
<!-- _header: "" -->

![bg right:45% contain](img/frog_gopigo.png)

![h:52](img/jfrog-conan-logo.png)

###### ROSCon España 2026 · Valencia

# ROS sin rodeos

## Desarrollo nativo en *C++* para robótica

**Daniel Manzaneque**
Ingeniero Software · Conan / JFrog

<!--
⏱ 0:00 → 0:25
Hola a todos. Soy Daniel Manzaneque y trabajo como ingeniero de software en el equipo de Conan, en JFrog.

Soy ingeniero industrial y, antes de dedicarme al software, trabajé con robots. De hecho, mi tesis la hice con ROS 1, en tiempos de Indigo.

Hoy os quiero contar cómo usar ROS sin rodeos: una experiencia de desarrollo nativa en C++.
-->

---

###### De dónde venimos...

## Un robot pequeño con un ordenador *modesto*

- Una placa con pocos recursos (tipo Raspberry Pi)
- Control y percepción escritos en **C++**
- **ROS 2** para hablar con sensores, herramientas y otros equipos


<!--
⏱ 0:25 → 0:50
Para contarlo voy a usar un ejemplo que nos acompañará toda la charla: un robot pequeño, con un ordenador modesto, tipo Raspberry Pi.

Buena parte del software ya está hecho en C++: el control de bajo nivel de los motores y la lectura de los sensores.

Y en algún momento quise añadirle ROS 2, para que hablase con otros nodos y herramientas. Pero...
-->

---

###### El punto de partida

## «Solo quería publicar un topic desde mi código *C++*»

Antes de escribir una línea útil, hay que:

1. Tener la versión de Ubuntu que pide la distro
2. Instalar con `apt` y `rosdep` todo lo demás
3. Crear un workspace de colcon con su estructura
4. Escribir `package.xml` y adaptar el CMake a `ament_cmake`
5. Acordarse de hacer `source setup.bash`
6. ...

**Muchos pasos antes de llegar al robot**

<!--
⏱ 0:50 → 1:25
Yo solo quería que mi código C++ hablase ROS. Que pudiera comunicarse con otros nodos para tareas más complejas, como navegación o SLAM, o para incorporar otros sensores.

Pero antes de escribir una sola línea útil tenía que usar la versión de Ubuntu que pide la distro. Instalar un montón de paquetes de sistema que ni sabía para qué servían. Crear un workspace, convertir mi proyecto en un paquete de ROS y acordarme de ejecutar los scripts de entorno.

Muchos pasos antes de llegar al robot.
-->

---

<!-- _class: cards -->

###### El mapa de la charla

## Tres rodeos *mejorables*

1. **Instalar** ROS se instala en el sistema → ROS pasa a ser **una dependencia más**.
2. **Desarrollar** Tu proyecto se adapta a ROS → Tu **proyecto C++ de siempre**.
3. **Desplegar** Compilar en el robot o en la imagen de despliegue → **Construir fuera**, llevar solo lo necesario.

<!--
⏱ 1:25 → 2:35
A estos pasos los llamo rodeos: cosas que haces no porque aporten algo a tu robot, sino porque la herramienta te lo exige.

Después de un tiempo volví a ROS y vi que la experiencia seguía siendo muy parecida. En el equipo de Conan nos fijamos en tres rodeos que creemos que se pueden simplificar.

Al instalar: en lugar de instalar ROS en el sistema, tratarlo como una dependencia más, como cualquier librería.

Al desarrollar: en lugar de adaptar tu proyecto a ROS, seguir con tu proyecto C++ de siempre.

Y al desplegar: en lugar de compilar en el robot o dentro de la imagen de despliegue, construir fuera y llevar solo lo necesario.

Y quiero ser justo desde el principio: estos rodeos tienen su razón de ser. ROS tuvo que resolver problemas que iban más allá de la robótica, como distribuir binarios, orquestar cientos de paquetes o preparar entornos. Y los resolvió con herramientas que llevan años funcionando, por eso las usamos todos. Lo que os traemos es otro camino para cuando esos rodeos duelen.
-->

---

<!-- _class: herramienta -->

###### La herramienta

## Conan, el gestor de paquetes *open source* de C y C++

#### Código abierto (MIT)
- Mantenido por el equipo de Conan con el feedback de la comunidad

#### Cada librería es una **receta**
- Hay unas 2.000 recetas en ConanCenter y puedes crear las tuyas.

#### Agnóstico al build-system
- Compatible con CMake, Bazel, Meson, MSBuild...

#### Resuelve el **grafo** completo de dependencias transitivas
- Obtiene un **binario por configuración**, si no está disponible lo compila desde el código fuente.


<!--
⏱ 2:35 → 3:50
Y aquí entra Conan, la herramienta que nos permite hacer todo esto.

[Pregunta al público y pausa] ¿Conocéis Conan? ¿Habéis oído hablar de Conan? (No me refiero al bárbaro.)

Conan es un gestor de paquetes de software y binarios para C y C++. Lo que pip es para Python, Conan lo es para C y C++.

- Es un proyecto open source, desarrollado con el feedback y la colaboración de los usuarios. Todo el código de la herramienta es abierto, igual que el de las recetas.

- Cada librería se describe en una receta o conanfile. Las recetas para librerías open source viven en ConanCenter, el repositorio público. Además, cualquiera puede tener su propio servidor donde alojar sus recetas y binarios.

- Es compatible con cualquier sistema de build. CMake es el que mejor integración tiene, pero también Bazel, Meson, MSBuild o el vuestro propio.

- No solo gestiona paquetes, sino también binarios. Un binario por configuración: sistema, arquitectura, compilador, Debug o Release. Si el binario no existe, Conan puede ejecutar la receta y compilarlo desde fuentes.
-->

---

<!-- _class: problema -->

###### Rodeo 1 · Instalar

## Una versión por sistema. Una imagen *por distro*

- **`apt` y `rosdep`**: instalan la versión que trae la distro. `package.xml` declara dependencias, pero no elige versiones
- **Docker**: congela esa foto y la hace repetible. Otra distro de ROS, otra imagen
- ¿Otra versión de una librería? La compilas a mano y nadie comprueba que no choque con la de ROS
- Y el desarrollo se muda dentro de la imagen, lejos de tu IDE

> `apt` y Docker resuelven bien la instalación. Lo que no ven es el grafo de tu proyecto.

<!--
⏱ 3:50 → 4:55
Una vez que sabemos lo que es Conan, empecemos por el primer rodeo: la instalación de ROS.

Todos los que estáis aquí habéis instalado ROS alguna vez. Se hace con apt y rosdep, y depende de la versión de Ubuntu que tengáis. Ya ni hablamos de desarrollar en una plataforma que no sea Ubuntu.

La solución habitual, y muy razonable, son las imágenes de Docker: una por distro de ROS, con su Ubuntu, a la que sumáis vuestro software. Funciona y es repetible.

Pero dentro de la imagen, apt y rosdep siguen instalando lo que trae la distro. Si necesitáis otra versión de una librería, la añadís a mano y os aseguráis de que no choca con la del sistema. Y eso, una vez por cada imagen.

Ni el sistema ni el contenedor conocen el grafo de dependencias de vuestro proyecto. Y además os llevan a desarrollar dentro de la imagen, algo que veremos en el segundo rodeo.

[Si encaja: la charla anterior en esta sala habla de testing multidistro. Se puede enlazar con ella.]
-->

---

<!-- _class: solucion -->

###### Sin rodeos

## ROS es *una dependencia más*

###### `conanfile.txt`

```ini
[requires]
ros-kilted/2026.06.17
opencv/4.12.0
```

- ROS vive en la **caché de Conan**, no en `/opt/ros` ni en una imagen
- Varias distros de ROS en la misma máquina, **sin una imagen por distro**

```bash
conan install conanfile.txt --build=missing
```

- El mismo flujo en **Linux, macOS y Windows**

<!--
⏱ 4:55 → 5:40
¿Cómo lo resuelve Conan? Tratando a ROS como una dependencia más.

Esto es un conanfile.txt, el equivalente a un requirements.txt de Python. Aquí ROS Kilted aparece como una dependencia de mi proyecto, igual que cualquier otra librería, por ejemplo OpenCV.

Conan instala ROS en su caché, que es una carpeta en vuestro espacio de usuario. No va a /opt/ros ni a una imagen, así que no choca con las librerías del sistema. Y como cada versión vive en su propia carpeta, podéis tener varias distros de ROS en la misma máquina y elegir cuál usa cada proyecto.

Para instalarlo todo basta un conan install. Y es la misma experiencia en Linux, en macOS y en Windows.
-->

---

<!-- _class: solucion -->

###### El paquete

## ¿Qué es *`ros-kilted`*?

- **ROS 2 Kilted compilado desde fuentes**, empaquetado como un único paquete Conan
- **Versión = sincronización de rosdistro**: `2026.06.17` es el tag `kilted/2026-06-17`
- **Variantes** como los metapaquetes oficiales: `core`, `base`, `desktop`
  `-o ros-kilted/*:variant=desktop`
- Las **dependencias de terceros** (OpenSSL, Eigen, yaml-cpp, OpenCV…) vienen de ConanCenter: son nodos del grafo
- Incluye `ros2` y `colcon`: RViz y los **tutoriales oficiales** siguen funcionando

<!--
⏱ 5:40 → 6:30
¿Y qué es exactamente ese ros-kilted?

Es ROS 2 Kilted compilado desde fuentes con colcon, como haríais vosotros, pero dentro de una receta de Conan. El resultado es un único paquete.

La versión es una fecha: corresponde al tag de sincronización de rosdistro. 2026.06.17 es exactamente el snapshot kilted del 17 de junio.

Tiene variantes que siguen los metapaquetes oficiales: core, base y desktop. Con desktop tenéis RViz y las herramientas gráficas.

Las librerías de terceros que usa ROS, como OpenSSL, Eigen, yaml-cpp u OpenCV, no van dentro: vienen de ConanCenter y son nodos del grafo. Eso es importante para lo que viene ahora.

Y trae el CLI de ros2 y colcon, así que los tutoriales oficiales siguen siendo válidos.
-->

---

<!-- _class: problema grafo -->

###### El grafo

## ROS, OpenCV y Eigen en el *mismo* grafo

![w:1080](img/grafo.svg)

**Este grafo no cierra.**

- `ros-kilted` (variante `desktop`) usa OpenCV 4.12. Mi nodo quiere la nueva 4.14
- En C++, dos OpenCV son **dos `cv::Mat`** en el mismo programa
- Conan lo detecta **al instalar**, antes de compilar una línea

<!--
⏱ 6:30 → 7:30
Como Conan conoce el grafo completo, puede comprobar que sea consistente. Mirad este caso.

Mi nodo depende de ROS Kilted y de OpenCV 4.14, la última versión, porque necesito algo que solo está ahí: una función nueva, un arreglo o mejor rendimiento. Pero ROS, en la variante desktop, usa OpenCV 4.12. Y cada OpenCV trae su propia libpng.

Eigen sale en verde: aparece una sola vez y todos comparten la misma. Lo rojo son paquetes repetidos con versiones distintas.

En C++ cada cosa debe tener una sola definición. Con dos OpenCV tendríamos dos cv::Mat en el mismo programa: puede fallar al enlazar o, peor, enlazar y fallar en ejecución.

Con apt, la distro solo trae una OpenCV. Si compiláis otra a mano, en el sistema o en la imagen, nadie comprueba si choca con la de ROS. Conan os avisa del conflicto al instalar.
-->

---

<!-- _class: solucion -->

###### El grafo · solución

## Si no cierra, *decides tú* y Conan recompila

###### `conanfile.py`

```python
class MiNodo(ConanFile):
    default_options = {"ros-kilted/*:variant": "desktop"}

    def requirements(self):
        self.requires("ros-kilted/2026.06.17")
        self.requires("opencv/4.14.0", force=True)
```

```bash
conan install conanfile.py --build=missing
```

- `force=True`: tu versión manda en todo el grafo, **también dentro de ROS**
- Lo que dependía de OpenCV se recompila: **un solo `cv::Mat`**
- Antes: compilar otra OpenCV dentro de la imagen y esperar que no choque

<!--
⏱ 7:30 → 8:15
¿Y cómo se arregla? Lo decide el usuario.

Para esto pasamos del conanfile.txt a un conanfile.py, que permite decir algo más de cada dependencia. Pedimos OpenCV 4.14 con force=True: esta versión manda en todo el grafo, también por encima de la que pide ROS.

Al instalar con --build=missing, Conan ve que el binario de ROS que tiene ya no corresponde a esa OpenCV, y lo recompila. El resultado es un grafo consistente, con un solo cv::Mat.

Antes, con apt o en una imagen, compilabais otra OpenCV dentro y esperabais que no chocara con la de ROS.

Siendo honestos: hoy la receta de ROS es monolítica, así que recompilar ROS es recompilarlo entero. Volveré a esto al final.
-->

---

<!-- _class: problema -->

###### Rodeo 2 · Desarrollar

## Para usar ROS, tu proyecto tiene que *«hacerse ROS»*

- La estructura del workspace: `src/ build/ install/ log/`
- `package.xml` y macros de `ament_cmake` dentro de tu CMake
- `colcon build` en lugar de tu build de siempre
- El IDE no encuentra nada si no hiciste `source` antes de abrirlo
- Librerías de terceros: unas de `apt`, otras copiadas al repo, otras a mano

> Si ROS es solo una capa de un producto C++ grande, el rodeo lo paga **todo** el producto.

<!--
⏱ 8:15 → 9:05
Vamos con el segundo rodeo: desarrollar. Hoy, para usar ROS, tu proyecto tiene que hacerse ROS.

Tienes que seguir la estructura del workspace. Escribir un package.xml y meter macros de ament_cmake en tu CMake. Compilar con colcon en lugar de con tu build de siempre. Y acordarte de hacer source antes de abrir el IDE, o no encontrará nada.

Para muchos de vosotros, que empezáis los proyectos desde cero en ROS, esto quizá no sea un problema, aunque condiciona cómo desarrolláis.

Pero pensad en mi robot, o en una empresa con años de código C++ de control, visión o planificación que quiere hablar ROS. Tiene que reorganizar el proyecto alrededor de las convenciones de ROS, o mantener dos mundos en paralelo.
-->

---

<!-- _class: problema -->

###### Rodeo 2 · Desarrollar

## Desarrollar *dentro* de la imagen

- Compilas con las herramientas que trae la imagen, que suele ser también la del robot
- El IDE no vive ahí: el índice, los breakpoints y el depurador cruzan el contenedor
- Volúmenes, permisos y `docker exec`: más pasos en cada ciclo de compilar y depurar

> Los dev containers ayudan mucho. Aun así, la imagen brilla más al desplegar que al desarrollar.

<!--
⏱ 9:05 → 9:50
Y a esto se suma lo que vimos en el primer rodeo. Si ROS vive en una imagen de Docker, vuestro desarrollo también vive dentro de esa imagen.

Primero, compiláis con lo que tenga la imagen. Si es la misma para el portátil y para el robot, o el robot acaba cargando con todo el toolchain de desarrollo, o mantenéis dos imágenes.

Segundo, el IDE no vive ahí. Los dev containers lo resuelven bastante bien, y si os funcionan, adelante. Pero siguen siendo un puente entre el IDE y el contenedor.

Y tercero, cada ciclo pasa por volúmenes, permisos y docker exec.

Para nosotros, donde la imagen brilla de verdad es al desplegar en el robot.
-->

---

<!-- _class: solucion -->

###### Sin rodeos

## Un proyecto CMake normal que *usa* ROS

###### `CMakeLists.txt`

```cmake
find_package(rclcpp REQUIRED)
find_package(OpenCV REQUIRED)

add_executable(my_node src/main.cpp)
target_link_libraries(my_node PRIVATE rclcpp::rclcpp opencv::opencv)
```

Instalar dependencias y compilar:

```bash
conan install conanfile.txt --build=missing
cmake --preset conan-release
cmake --build --preset conan-release
```

<!--
⏱ 9:50 → 10:45
Entonces, ¿qué pinta tiene esto con Conan? Un proyecto CMake normal que usa ROS.

Como ROS es una dependencia más, Conan expone sus librerías a través del find_package de siempre. Aquí veis rclcpp exactamente igual que OpenCV.

Y los pasos son los habituales. conan install resuelve las dependencias y genera los ficheros que necesita CMake. Después, CMake configura y compila el proyecto. Sin workspace, sin colcon y sin hacer source de nada. Y lo podéis abrir directamente en vuestro IDE.

Es justo lo que hice con mi robot. El código de motores y sensores que ya tenía no cambió de estructura. Le añadí un conanfile.txt, un par de líneas en el CMake, y empezó a publicar sus topics.

Lo enseño con CMake porque es casi el estándar de facto, pero lo mismo aplica a cualquier otro sistema de build.
-->

---

<!-- _class: pose -->

###### Ejemplo real · examples/pose_estimation

## Estimación de pose humana: *ROS + visión + ML*

```text
pose_estimation/
├── CMakeLists.txt
├── conanfile.txt
├── src/pose-estimation.cpp
└── assets/  # ML models
```

- Sin `package.xml`, sin `ament`, sin workspace.
- `ros-kilted`, `opencv` y `tensorflow-lite`, en un solo grafo.
- Todo se instala con un `conan install`

<!--
⏱ 10:45 → 11:25
Un ejemplo real del repositorio: estimación de pose humana. Un modelo de machine learning, bueno, ahora se dice IA, estima la posición del cuerpo de una persona y publica los puntos en un topic de ROS.

A la izquierda veis la imagen de la cámara con el esqueleto detectado. A la derecha, RViz recibiendo esos puntos, lanzado también desde Conan con la variante desktop.

El proyecto son unos pocos ficheros: sin workspace de colcon y sin package.xml. Tiene tres dependencias directas, ROS Kilted, OpenCV y TensorFlow Lite, y todas se resuelven en un único grafo con un conan install.
-->

---

<!-- _class: solucion -->

###### ¿Ya tienes un workspace de colcon?

## Conan *dentro* de tu workspace

###### `mi_paquete/conanfile.txt`

```ini
[requires]
tensorflow-lite/2.15.0

[generators]
CMakeDeps
CMakeToolchain
ROSEnv
```

```bash
conan install mi_paquete/conanfile.txt --build=missing
source /opt/ros/kilted/setup.bash       # tu ROS de siempre
source install/conan/conanrosenv.sh
colcon build
```

<!--
⏱ 11:25 → 12:10
Vale, ¿y si ya tenéis un desarrollo en ROS, con vuestro workspace de colcon? Que será el caso de la mayoría.

No hay problema. Lo anterior es como creemos que debería ser la experiencia nativa, pero también podéis hacer el camino inverso: meter Conan dentro de ROS. Y esta es probablemente la forma más fácil de empezar.

El año pasado añadimos a Conan el generador ROSEnv. Funciona así: en el paquete que necesita una librería de terceros, añadís un conanfile.txt con esa librería, por ejemplo TensorFlow Lite, y el generador ROSEnv.

Hacéis conan install, activáis vuestro ROS de siempre, el de apt, después el entorno de Conan, y colcon build como siempre.
-->

---

<!-- _class: solucion -->

###### ¿Ya tienes un workspace de colcon?

## Qué hace *ROSEnv*

- Genera `conanrosenv.sh/bat`: colcon y CMake encuentran las librerías de Conan
- En tu `CMakeLists.txt`, nada específico de Conan:
  `find_package(tensorflowlite)`
- Funciona con **tu ROS de `apt`** o con **`ros-kilted` desde Conan**
- Sin tocar el sistema y sin copiar código de terceros al workspace

> No cambias tu flujo: es la puerta de entrada más sencilla.

<!--
⏱ 12:10 → 12:50
¿Qué hace exactamente ROSEnv? Genera un script de entorno con lo necesario para que colcon y CMake encuentren las librerías que ha instalado Conan, y para que se encuentren también al ejecutar.

En vuestro CMakeLists no hay nada específico de Conan: un find_package de siempre.

Funciona tanto con el ROS que tenéis instalado con apt como con ros-kilted desde Conan. Y no toca el sistema ni os obliga a copiar código de terceros al workspace.

Así que si solo os quedáis con una cosa de esta charla, que sea esta: podéis probar Conan mañana en vuestro workspace sin cambiar nada más.
-->

---

<!-- _class: problema -->

###### Rodeo 3 · Desplegar

## Llevar el código *al robot*

- **Compilar en el robot**: viable en una Jetson, muy lento en una placa modesta
- **Replicar el entorno de desarrollo en el robot**: herramientas y dependencias que el robot no necesita para funcionar
- **Copiar la carpeta `install/`**: rutas absolutas y librerías que faltan o sobran en el robot
- **¿Qué hay realmente instalado en el robot?** Difícil de contestar cuando lo pregunta un cliente, una auditoría o aparece un CVE

<!--
⏱ 12:50 → 13:30
Y llegamos al último rodeo: desplegar. ¿Cómo llevamos el código al robot?

¿Compilamos en el robot? En una Jetson se puede, pero con una placa como la mía es lentísimo. ¿Replicamos el entorno de desarrollo en el robot? Acaba cargando con compiladores, cabeceras y herramientas que no necesita para funcionar. ¿Copiamos la carpeta install? Lleva rutas absolutas, y faltan las librerías de ROS del sistema. ¿Cuáles necesito y cómo las copio?

Y una pregunta más: ¿qué hay realmente instalado en el robot? Si os lo pregunta un cliente, una auditoría o aparece un CVE, ¿sabríais contestar?
-->

---

<!-- _class: solucion cruzado -->

###### Sin rodeos

## Compilar en tu máquina, *ejecutar en el robot*

###### `robot_arm64` · perfil host
```ini
[settings]
os=Linux
arch=armv8
compiler=gcc
compiler.version=13
[tool_requires]
arm-gnu-toolchain/13.3
```

```bash
conan install conanfile.txt --profile:build=default --profile:host=robot_arm64
```

- **Build**: tu portátil, donde corren CMake y el compilador cruzado
- **Host**: el robot (ARM), al que van tu código y sus librerías

<!--
⏱ 13:30 → 14:50
Conan resuelve esto separando dos contextos, y cada uno se describe en un perfil.

El contexto de build es tu portátil. Ahí corren las herramientas: CMake, el CLI de ros2 y el compilador cruzado. El contexto de host es el robot, con su arquitectura ARM. Para él van tu código y sus librerías.

Esto es el perfil del robot. Describe el sistema operativo, la arquitectura, el compilador y su versión. En general, todo lo que afecta al binario generado.

Además, el perfil pide el compilador cruzado como un paquete más. Aquí es el Arm GNU Toolchain, empaquetado en una receta propia. También podría ser el que da el fabricante de la placa. Conan lo instala con su versión fija, así que todo el equipo compila exactamente con el mismo compilador.

Al hacer conan install le pasáis los dos perfiles, y Conan genera el toolchain de CMake para compilar en cruzado. Luego compiláis exactamente igual que antes.

En mi caso, el portátil hace todo el trabajo pesado y la placa del robot solo se dedica a ejecutar.

Y si los binarios de alguna dependencia no existen para el robot, se compilan una vez y se suben a vuestro servidor, para que la próxima vez se reutilicen.
-->

---

<!-- _class: solucion -->

###### Sin rodeos

## Llevar al robot *solo lo que necesita*

```bash
conan install conanfile.txt -pr:h=robot_arm64 --deployer=runtime_deploy --deployer-folder=robot
```

- Viaja solo el **runtime**: los ejecutables y las librerías dinámicas que tu nodo necesita para arrancar
- Se quedan en tu máquina las **herramientas de build**: CMake, compiladores, cabeceras, generadores
- Una carpeta: `scp` o una imagen mínima. El robot **no necesita Conan**

<!--
⏱ 14:50 → 15:50
Y por último, ¿qué llevamos al robot? Para eso Conan tiene los deployers: scripts que recogen lo necesario de cada paquete y lo dejan en una carpeta.

Como Conan sabe qué tipo de paquete es cada uno y en qué contexto se usa, puede separar lo que se ejecuta de lo que solo sirve para compilar. runtime_deploy copia solo los ejecutables y las librerías dinámicas: lo que vuestro nodo necesita para arrancar en el robot. CMake, los compiladores, las cabeceras y todo lo que solo sirve para compilar se queda en vuestra máquina.

El resultado es una carpeta. La copiáis con scp o la metéis en una imagen mínima, y el robot no necesita Conan.

Con mi robot, lo que viaja es mi nodo y las librerías de ROS que usa, nada más. Ocupa mucho menos que una imagen con todo el entorno de desarrollo, y desplegar una versión nueva es un scp.

[Si tengo el dato: X MB de la carpeta frente a Y GB de la imagen.]
-->

---

<!-- _class: solucion -->

###### Sin rodeos

## Qué va en cada robot: *lockfile y SBOM*

```bash
conan lock create . -pr:h=robot_arm64 --lockfile-out=robot.lock
conan install . -pr:h=robot_arm64 --lockfile=robot.lock   # genera sbom.cdx.json
conan audit list --sbom=sbom.cdx.json
```

- **El cliente** pregunta qué versión lleva su robot: el **lockfile** fija todo el grafo, hoy y dentro de un año
- **La auditoría** pide el **SBOM**: el inventario de todo el software del robot, en CycloneDX, generado con un hook en `conan install`
- **Aparece un CVE**: `conan audit` revisa ese SBOM contra vulnerabilidades conocidas

<!--
⏱ 15:50 → 16:50
Y volvemos a la pregunta incómoda del rodeo 3: si os pregunta un cliente, una auditoría o aparece un CVE, ¿sabéis qué hay en cada robot?

Primero, el cliente. conan lock create guarda las versiones y revisiones exactas de todo el grafo. Si instaláis con ese lockfile, hoy o dentro de un año, obtenéis exactamente lo mismo: la release que llevasteis a ese cliente. Y para quien investiga, es poder reproducir el entorno de un experimento o de un artículo años después.

Segundo, la auditoría. Cada conan install deja un SBOM en CycloneDX, generado a partir del mismo grafo. Un SBOM es el inventario del software: la lista de componentes y versiones que va en el robot. Es algo que cada vez se exige más a los fabricantes, junto con la obligación de notificar vulnerabilidades.

Y tercero, el CVE. conan audit lee ese SBOM y lo revisa contra una base de vulnerabilidades conocidas.
-->

---

<!-- _class: video -->

###### Volviendo a mi robot

## Mi robot, *sin rodeos*

![w:660](img/robot-roscon-global.gif)

ROSCon Global 2026 · Toronto

<!--
⏱ 16:50 → 17:25
Y volviendo a mi robot pequeño, el del principio.

Aquí lo tenéis en el stand de Conan en ROSCon Global, en Toronto, siguiendo la línea del circuito.

El mismo código C++ de siempre, hablando ROS, sin haber instalado ROS en el robot.
-->

---

###### Resumen

## Los tres rodeos, *simplificados*

| | Habitual | Conan |
|---|---|---|
| Instalar | El sistema, o una imagen por distro | Una dependencia más en la caché. Grafo consistente |
| Desarrollar | Workspace, `package.xml`, `ament`, `colcon` | CMake de siempre y `find_package`. O ROSEnv en tu workspace |
| Desplegar | Compilar en el robot, replicar el entorno o copiar `install/` | Perfiles build/host, `runtime_deploy`, lockfile y SBOM |

<!--
⏱ 17:25 → 17:55
Resumiendo. Para instalar, ROS pasa a ser una dependencia más, en una caché donde conviven varias versiones y con un grafo consistente. Para desarrollar, vuestro CMake de siempre con find_package, o ROSEnv si ya tenéis un workspace de colcon. Y para desplegar, perfiles de build y host, un deployer que lleva al robot solo el runtime, y un lockfile y un SBOM para saber qué va en cada robot.
-->

---

###### Siendo honestos

## Es una *prueba de concepto*

- **Receta monolítica**: toda la distro en un paquete. Cambiar una dependencia recompila ROS entero
- **Sin binarios precompilados**: el primer `conan install` compila ROS desde fuentes
- **Solo ROS Kilted**, con las variantes `core`, `base` y `desktop`
- **Sin probar a fondo**: interfaces propias (IDL) fuera de colcon, paquetes fuera de las variantes (Nav2, MoveIt…)

<!--
⏱ 17:55 → 18:55
Hay que ser honestos y también explicar las limitaciones

Esto es una prueba de concepto que hemos llevado a cabo para poner de manifiesto los puntos en los que creemos que una herramienta como Conan puede ayudar a los desarrolladores de ROS

Evidentemente, hay aspectos mejorables pero que no invalidan los puntos anteriores. Cosas como:

- La receta es monolítica: toda la distro va en un único paquete. Es lo más sencillo para empezar, pero tiene un coste: si cambiáis una dependencia, como la OpenCV de antes, se recompila ROS entero.

- No hay binarios precompilados. El primer conan install compila ROS desde fuentes, y eso lleva su tiempo. Después queda en la caché o en vuestro servidor y no se repite.

- Disponemos de ROS Kilted, que puede consumirse en sus variants core, base y desktop.

Y hay cosas que no hemos probado, habrá cosas que se nos escapen, pero aquí es cuando entráis vosotros.
-->

---

###### Pruébalo hoy

## Necesitamos *vuestro feedback*

- Recetas y ejemplos en [github.com/conan-io/ros-conan](https://github.com/conan-io/ros-conan)
- Probado en CI: **Linux** (x86_64 y arm64), **macOS** y **Windows**
- **Ejemplos**: CMake puro, workspace de colcon, pose_estimation (OpenCV + TensorFlow Lite)

Issues, ideas y críticas: **todas bienvenidas**

<!--
⏱ 18:55 → 19:35
Todo lo que os he contado lo podéis probar ya. Las recetas y los ejemplos están en el repositorio ros-conan, probados en CI en Linux, también en ARM, en macOS y en Windows. Hay ejemplos con CMake puro, con un workspace de colcon y el de estimación de pose.

Cada caso es un mundo, y por eso necesitamos conocer los vuestros. Si os falta un paquete, una distro o una plataforma, abrid un issue.

Si esto os resulta familiar, si habéis sufrido estos rodeos, echadle un vistazo, probad y contadnos. Estaré encantado de hablar con vosotros después.
-->

---

<!-- _class: mascota -->
<!-- _footer: "[![Conan](img/conan-cube.png) `conan.io`](https://conan.io) [`github.com/conan-io/ros-conan`](https://github.com/conan-io/ros-conan)" -->
<!-- _paginate: false -->
<!-- _header: "" -->

![bg right:38% contain](img/frog_turtle2.png)

###### ¡Gracias!

# ¿*Preguntas*?

Prueba los ejemplos:
- [github.com/conan-io/ros-conan](https://github.com/conan-io/ros-conan/tree/main/examples)

Más info:
- *Bringing ROS into your native C/C++ workflow with Conan* - `discourse.openrobotics.org`
- *Robotics with Conan: consuming ROS as a regular package* - `blog.conan.io`

<!--
⏱ 19:35 → 19:50. Preguntas hasta 20:00.
Y nada más, muchas gracias a todos. Si tenéis preguntas, este es el momento, y si no da tiempo, lo comentamos después. ¡Gracias!
-->
