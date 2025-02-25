Este proyecto es un clon de Airbnb llamado HBnB, desarrollado con una arquitectura modular en Python. En esta primera etapa se configura la estructura inicial del proyecto, estableciendo las capas de Presentación, Lógica de Negocio y Persistencia, y se implementa un repositorio en memoria junto con el patrón Facade para facilitar la comunicación entre las capas.

La organización del proyecto es la siguiente:

hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       └── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── facade.py
│   └── persistence/
│       ├── __init__.py
│       └── repository.py
├── run.py
├── config.py
├── requirements.txt
└── README.md



Descripción de las Capas



Presentación:

Se encarga de la interacción con el usuario a través de la API. Utiliza Flask y Flask-RESTx para definir rutas y manejar las peticiones HTTP.

Lógica de Negocio:

Contiene las reglas y procesos centrales del sistema. Aquí se definen las clases y métodos que gestionan la creación, actualización y procesamiento de datos, sin preocuparse por cómo se presentan o almacenan.

Persistencia:

Inicialmente, se utiliza un repositorio en memoria para el almacenamiento y validación de objetos. Esta capa está diseñada para poder ser sustituida en el futuro por una solución basada en bases de datos (por ejemplo, utilizando SQL Alchemy).

Facade (Fachada):

El patrón Facade se implementa en la capa de servicios para simplificar la interacción entre las diferentes capas del sistema, proporcionando una interfaz única y centralizada para acceder a las operaciones de negocio.


Instalación

Clonar el repositorio:

git clone <https://github.com/SFerFer1/holbertonschool-hbnb>



Ingresar al directorio del proyecto:

cd hbnb



Instalar las dependencias:

pip install -r requirements.txt
Ejecución de la Aplicación


Para iniciar la aplicación Flask, ejecuta:

python run.py
