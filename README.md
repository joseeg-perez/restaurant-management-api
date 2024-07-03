# Restaurant Management API

Proyecto realizado para la asignatura de Desarrollo de APIs en Python en la Universiadad Católica Andrés Bello.

El objetivo de este proyecto es desarrollar el backend de un sistema de gestión para un restaurante. El sistema permitirá a los administradores del restaurante gestionar inventarios de ingredientes, elaborar menús, procesar pedidos de los clientes, y generar reportes diversos.

<h2 align="center">🧰 Stack de desarrollo 🧰</h2>
<p align="center"> 
    <a href="https://www.python.org/" target="_blank"
      rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"
      alt="javascript" width="100" height="100" /> </a>
    </a>
    <a href="https://fastapi.tiangolo.com/" target="_blank"
      rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/fastapi/fastapi-original.svg"
      alt="javascript" width="100" height="100" /> </a>
    </a>
    </a>
    <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> 
    <a href="https://www.postgresql.org/" target="_blank" rel="noreferrer"> <img
      src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg"
      alt="react" width="100" height="100" /> 
    </a>
    <img
      src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg"
      alt="react" width="100" height="100" /> 
    </a>

</p>
<br/>

<h2 align="center">⚙️ Instalación del proyecto ⚙️ </h2>

1. Clonar el repositorio 
```
git clone https://github.com/joseeg-perez/restaurant-management-api.git
```

2. Acceder al directorio del proyecto
```
cd restaurant-management-api
```

3. Renombrar el archivo ```.env.template``` a ```.env``` y llenar las variables de entorno respectivas

4. Levantar el contenedor de Docker 
```
docker-compose up --build
``` 

<h2 align="center">☑️ Probar los Endpoints ☑️ </h2>

Una vez levantado el contenedor de docker la aplicacion estará corriendo de forma local. Para probar los endpoints se debe acceder a la siguiente URL donde encontraremos la documentación respectiva de la API con todos los detalles necesarios para su funcionamiento.
```
http://http://localhost:8000/docs
```

<h2 align="center"> 📁 Base de datos 📁</h2>

La base de datos está alojada en Railway, por lo que no se necesita ejecutar ningún comando adicional para configurarla. La API se conectará automáticamente a la base de datos remota.


## Autores
- [Luis Montes](https://github.com/luiselianm)
- [José Pérez](https://github.com/joseeg-perez)
- [Joyce Wagner](https://github.com/joycewagnerr)