# Git - sistema de control de versiones


## Trabajo previo

### Tutoriales
Abba, I. V. (2021). *Git and GitHub Tutorial – Version Control for Beginners*. FreeCodeCamp.Org. https://www.freecodecamp.org/news/git-and-github-for-beginners/

### Otros
Instale en su computadora el sistema de control de versiones [Git](https://git-scm.com/downloads).

Instale en su computadora un editor de código fuente, por ejemplo:
- [Notepad++](https://notepad-plus-plus.org/)
- [Visual Studio Code](https://code.visualstudio.com/)

## Descripción general
[Git](https://git-scm.com/) es un sistema de [control de versiones](https://es.wikipedia.org/wiki/Control_de_versiones) diseñado para "rastrear" cambios en el código fuente durante el proceso de desarrollo de software. Sin embargo, puede ser utilizado para llevar el control de los cambios en cualquier conjunto de archivos (ej. [documentación](https://guides.github.com/features/wikis/), [música](https://techcrunch.com/2013/10/09/splice-music/)). 

Un sistema de control de versiones proporciona, entre otras ventajas:

* La capacidad de recuperar versiones anteriores de los archivos.
* La capacidad de integrar modificaciones efectuadas por varias personas en el mismo conjunto de archivos.
* La capacidad de mantener varias "ramas" (_branches_) de un producto (ej. "estable", "evaluación", "inestable", como en el caso de [Debian Linux](https://www.debian.org/releases/), [GRASS GIS](https://grass.osgeo.org/download/software/sources/) y muchos otros proyectos de software libre).
* Facilidades para mantener redundancia y respaldos de los archivos (ej. [Programa de respaldos de GitHub](https://archiveprogram.github.com/)). Esta es una facilidad que implementan algunos servicios en la nube.

Git fue diseñado por Linus Torvalds en 2005 durante del desarrollo del _kernel_ del sistema operativo Linux. Se caracteriza por ser un [sistema de control de versiones distribuido](https://es.wikipedia.org/wiki/Control_de_versiones_distribuido), lo que significa que el código fuente puede estar alojado en la estación de trabajo de cualquier miembro del equipo de desarrollo. No se requiere de un repositorio "central", pero también se puede trabajar de esa forma.

El protocolo de Git es utilizado en varios sitios que proveen servicios de alojamiento de software, entre los que están [SourceForge](https://sourceforge.net/), [Bitbucket](https://bitbucket.org/), [GitLab](https://about.gitlab.com/) y [GitHub](https://github.com/).


## Funcionamiento
Desde el punto de vista de un usuario de Git (ej. un programador), Git se utiliza para sincronizar la versión local (i.e. en la computadora personal del usuario) de un conjunto de archivos, llamado proyecto o repositorio, con la versión que está alojada en un sistema remoto (ej. GitHub). Cada repositorio se almacena en un directorio (carpeta) del sistema operativo. La sincronización se realiza principalmente a través de dos operaciones:

* **_push_**: para "subir" al repositorio remoto los cambios realizados en el repositorio local. Esta operación se realiza mediante el comando [git push](https://git-scm.com/docs/git-push). Es probable que el sistema remoto le solicite al usuario algún tipo de autenticación (ej. nombre de usuario y clave).
* **_pull_**: para "bajar" al repositorio local los cambios realizados en el repositorio remoto. Esta operación se realiza mediante el comando [git pull](https://git-scm.com/docs/git-pull).

Las operaciones _push_ y _pull_ se ilustran en la {numref}`figure-git-push-pull`.

```{figure} img/git-push-pull.png
:name: figure-git-push-pull

Operaciones _push_ y _pull_. Imagen de [Melinda Higgins](https://www.coursera.org/learn/reproducible-templates-analysis/lecture/NGbQv/git-and-github-part-1).
```

Antes de un _push_, el usuario debe seleccionar los archivos que desea subir mediante el comando [git add](https://git-scm.com/docs/git-add), el cual pasa los archivos a un "área de espera" (_staging area_). Luego debe usarse el comando [git commit](https://git-scm.com/docs/git-commit) para "guardar" los cambios pendientes en el área de espera. Cada _commit_ guarda el estado del conjunto de archivos en un momento específico (_snapshot_).

La relación entre estas operaciones de Git, se ilustra en la {numref}`figure-git-push-pull-commit`.

```{figure} img/git-push-pull-commit.png
:name: figure-git-push-pull-commit

Operaciones de Git. Imagen de [Steven Klavins](https://medium.com/@stevenklavins94/version-control-part-4-c9387cf5b33e).
```

En la {numref}`figure-git-stage-commit-push` se muestra el funcionamiento de Git mediante una comparación con el procesamiento de una compra en línea.

```{figure} img/git-stage-commit-push.png
:name: figure-git-stage-commit-push

Operaciones de Git y compras en línea. Imagen de [Melinda Higgins](https://www.coursera.org/learn/reproducible-templates-analysis/lecture/NGbQv/git-and-github-part-2).
```

Otras operaciones de Git de uso frecuente son:

* [git config](https://git-scm.com/docs/git-config): para especificar opciones globales de la sesión de Git (ej. nombre del usuario, dirección de corre electrónico).
* [git init](https://git-scm.com/docs/git-init): para inicializar un repositorio git.
* [git clone](https://git-scm.com/docs/git-clone): para clonar (i.e. copiar) un repositorio remoto en la computadora local.
* [git status](https://git-scm.com/docs/git-status): para revisar el estado de los archivos y, por ejemplo, saber cuales deben pasarse al área de espera.
* [git log](https://git-scm.com/docs/git-log): para revisar el historial de _commits_.
* [git show](https://git-scm.com/docs/git-show): para visualizar los cambios efectuados en los _commits_.
* [git reset](https://git-scm.com/docs/git-reset): para regresar al estado correspondiente a un _commit_ anterior.

## Ejemplos de uso
### Clonación de un repositorio remoto y sincronización de los cambios efectuados localmente

Para seguir este ejemplo:

0. Obtenga un _token_ de GitHub en la siguiente opción de menú de su perfil de usuario: *Settings - Developer settings - Personal access tokens*. Seleccione las operaciones de tipo "repo". Copie el _token_ en un lugar seguro, ya que lo necesitará para autenticarse en GitHub.
1. Realice un _fork_ a su cuenta en GitHub del repositorio localizado en la dirección [https://github.com/gf0657-programacionsig/2022-ii-tutorial-git-repo-ejemplo](https://github.com/gf0657-programacionsig/2022-ii-tutorial-git-repo-ejemplo). Obtendrá un repositorio llamado "https://github.com/[nombre-usuario]/2022-ii-tutorial-git-repo-ejemplo", en donde [nombre-usuario] es su nombre de usuario en GitHub.
2. En una terminal del sistema operativo, con el comando `git clone https://github.com/[nombre-usuario]/2022-ii-tutorial-git-repo-ejemplo`, clone a su computadora el repositorio que acaba de bifurcar.
3. Con un editor de texto, abra el archivo ```README.md```, agregue una línea y guarde el archivo.
4. Luego, ejecute los siguientes comandos desde la terminal. Nota: las líneas que empiezan con  ```# ``` son comentarios.

```shell
# a. Cambio al directorio del repositorio.
cd 2022-ii-tutorial-git-repo-ejemplo

# b. Parámetros de configuración: nombre y dirección de correo del usuario.
#    Debe cambiar [email-usuario] y [nombre-usuario] por sus propios datos.
git config --global user.email [email-usuario]
git config --global user.name [nombre-usuario]
# Para revisar los parámetros de configuración:
git config --global --list

# c. Revisión de los archivos con modificaciones.
git status

# d. Adición (add) de los archivos modificados al "área de espera".
#    El punto (.) indica que se agregarán todos los archivos modificados.
git add .

# e. Grabado (commit) del conjunto de archivos modificados,
#    junto con un mensaje explicativo:
git commit -m "Agregar línea 2"

# f. "Subida" (push) de las modificaciones al repositorio remoto.
#    En este paso, es posible que deba utilizar su nombre de usuario/clave
#    o su token de GitHub para autenticarse.
git push
```

5. Revise los cambios aplicados en el repositorio remoto en GitHub.
6. Agregue más líneas al archivo del repositorio local y sincronícelo con el remoto, realizando nuevamente los pasos del c al f para cada _commit_. Recuerde que los comentarios de cada ```commit``` deben reflejar los cambios que están siendo aplicados.

## Recursos de interés
*Git*. (s. f.). Recuperado 28 de agosto de 2022, de https://git-scm.com/

*GitHub Archive Program*. (s. f.). GitHub Archive Program. Recuperado 10 de abril de 2022, de https://archiveprogram.github.com/

Higgins, M. (s. f.). *Reproducible Templates for Analysis and Dissemination*. Coursera. Recuperado 11 de abril de 2022, de https://www.coursera.org/learn/reproducible-templates-analysis

Klavins, S. (2020). *Version Control part 1*. Medium. https://stevenklavins94.medium.com/version-control-part-1-c5f1b43127f6
