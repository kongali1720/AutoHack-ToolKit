from setuptools import setup, find_packages

setup(
    name='autohack-toolkit',
    version='1.0.0',
    author='KongAli1720',
    description='🔥 AutoHack Toolkit Kocak Buat Latihan dan Hiburan',
    packages=find_packages(),
    py_modules=[
        'launcher',
        'wifi_cracker_simulator',
        'email_spammer_fake',
        'ddos_attack_simulator',
        'wifi_passwords_generator',
        'fake_root_access'
    ],
    entry_points={
        'console_scripts': [
            'autohack=launcher:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
