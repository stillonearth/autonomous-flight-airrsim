# Автономный полет по заданному маршруту для квадрокоптера с использование гибридной НС в условиях отсутствия сигнала ГНСС

## Описание

В данной работе рассматривается практическое использование современных средств для обеспечения автономного полёта БПЛА при отсутствии спутникового сигнала.

В певой части этой работы рассматривается реализация такого сценария в симуляторе AirSim и реализация алгоритма в Python.

## Техническая часть

### 1. Установка AirSim

AirSim — свободный симулятор полета квадрокоптера для Windows, Linux и Mac. Он предоставляет среду для разработки и тестирования алгоритмов управления квадрокоптером, а также для обучения нейронных сетей. В данный момент (Декабрь 2022) поддержка AirSim прекращена, но он по-прежнему активно используется в сообществе.

Для установки AirSim необходимо выполнить следующие действия:

1. Скачайте https://microsoft.github.io/AirSim/use_precompiled/
2. Распакуйте архив и запустите исполняемый файл

### 2. Установка среды Python

1. Скачайте и установите Anaconda https://www.anaconda.com/products/distribution/start-coding-immediately
2. Создайте и активируйте окружение airsim

```bash
conda env create -f environment.yml python=3.10
conda activate airsim
```

### Библиотека Estimator

Реализация фильтра Калмана и визуальной одометрии [1] находится в библиотеке Estimator. Для установки библиотеки выполните следующие действия:

```bash
mkdir build
cd build
cmake ..
cmake --build . --target estimator --config Release
cmake --install .
```

## Математические модели

### Extended Kalman Filter

[Wikipedia Article](https://en.wikipedia.org/wiki/Extended_Kalman_filter)

## Результаты

### Испытание в симуляторе AirSim

### Полевые испытания

## Выводы

## Ссылки

[1] Quadcopter State Estimation with Kalman Filtering in C++, 2018, https://github.com/cwiz/udacity-flying-car-cpp-estimation/blob/master/WRITEUP.md
