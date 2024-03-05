from setuptools import setup

setup(
    author='Alex',
    author_email='madest92@mail.com',
    name='teaxyz',
    version='0.0.1',
    description='A simple package for https://app.tea.xyz/',
    url='https://github.com/madest92/teaxyz',
    project_urls={
        'Homepage': 'https://github.com/madest92/teaxyz',
        'Source': 'https://github.com/madest92/teaxyz',
    },
    py_modules=['hi_tea'],
    entry_points={
        'console_scripts': [
            'hi-tea=hi_tea:hello_tea_xyz'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
    install_requires=[
        'tea-xyz1',
        'tea-xyz2',
    ],
)
