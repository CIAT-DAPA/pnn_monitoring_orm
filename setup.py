from setuptools import setup, find_packages

setup(
    name="pnn_monitoring_orm",
    version='0.0.0',
    author="victor-993",
    author_email="v.hernandez@cgiar.com",
    description="ORM para la base de datos de la herramienta monitoreo financiero PNN",
    url="https://github.com/CIAT-DAPA/pnn_monitoring_orm",
    download_url="https://github.com/CIAT-DAPA/pnn_monitoring_orm",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "greenlet==3.0.1",
        "psycopg2==2.9.9",
        "SQLAlchemy==2.0.23",
        "typing_extensions==4.8.0",
    ]
)
