![](https://raw.githubusercontent.com/tonypithony/imageupscale/refs/heads/main/AA1Ajr5Y.png)

```bash
pip install opencv-python opencv-contrib-python
```
![](https://raw.githubusercontent.com/tonypithony/imageupscale/refs/heads/main/input.jpg)
 
```bash
zip upscaled.zip EDSR_x3.pb images_superres.py input.jpg upscaled.png
```
 
# Sources
 
* [EDSR_x3.pb](https://github.com/Saafke/EDSR_Tensorflow/blob/master/models/EDSR_x3.pb?ysclid=m82p25odgw139265703)
* [Улучшение изображений с помощью нейросети с OpenCV (в 3 шага)](https://blog.mihailgok.ru/images-upscale-sr-opencv/)


## Bonus

Если вы использовали гипервизор Hyper-V и в какой-то момент решили установить VirtualBox, то при запуске виртуальной машины столкнетесь с ошибкой «Не удалось открыть сессию для виртуальной машины»:  

Решить это можно, удалив компоненты Hyper-V в Windows: Панель управления — Программы и компоненты — Установка и удаление компонентов. Однако, если виртуальные машины Hyper-V вам нужны, это может быть неудобно.

Для того, чтобы иметь возможность запускать виртуальные машины VirtualBox при установленных компонентах Hyper-V, требуется выключить запуск гипервизора Hyper-V. Для этого запустите командную строку от имени администратора и введите следующую команду:

```bash
bcdedit /set hypervisorlaunchtype off
```

## Sources

* [Запуск VirtualBox и Hyper-V на одном компьютере](https://tokmakov.msk.ru/blog/item/429)
* [Download VirtualBox (Old Builds): VirtualBox 6.0](https://www.virtualbox.org/wiki/Download_Old_Builds_6_0)
* [Как установить VirtualBox и запустить свою первую виртуальную машину](https://skillbox.ru/media/code/kak-ustanovit-virtualbox-i-zapustit-svoyu-pervuyu-virtualnuyu-mashinu/)

![](https://raw.githubusercontent.com/tonypithony/imageupscale/refs/heads/main/neofrtch.PNG)
