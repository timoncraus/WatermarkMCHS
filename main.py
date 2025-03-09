# coding=utf-8
#!/usr/bin/env python
from PIL import Image
import os
import platform
def de():
	## Ввод данных
	userhome = os.path.expanduser('~')
	desktop = userhome + '/Desktop/'
	useros = platform.system()
	my_dir = os.path.abspath(os.curdir)
	if useros.lower().count('window') > 0:
		print('--- Запускаем приложение на Windows? Отлично ---')
	print('@Вас приветствует приложение по прибавлению ватермарков на фотографии. Брать буду я фотографии с папки "Ввод", а кидать в "Вывод". Все папки должны быть на рабочем столе.')
	g = input('Нажмите Enter, чтобы продолжить или введите что угодно, после нажав Enter, чтобы открыть настройки:')
	if g != '':
		print('@Вы вошли в режим настройки')
		print('1/3 Введите абсолютный путь до папки, исполняющая роль ввода или введите "1", чтобы путь папкой, в которой запускается приложение:')
		print('(по умолчанию папка "Ввод" на рабочем столе)')
		dir_name = str(input(''))
		if dir_name == '':
			dir_name = desktop + '\\Ввод'
		elif dir_name == '1':
			dir_name = my_dir
		if dir_name==my_dir:
			print('2/3 Введите абсолютный путь до папки, исполняющая роль вывода:')
		else:
			print('2/3 Введите абсолютный путь до папки, исполняющая роль вывода или введите "1", чтобы путь папкой, в которой запускается приложение:')
		print('(по умолчанию папка "Вывод" на рабочем столе)')
		dir2_name = str(input(''))
		if dir2_name == '':
			dir2_name = desktop + '\\Вывод'
		if dir_name != my_dir:
			if dir2_name == '1':
				dir2_name = my_dir
		print('3/3 Введите ЦИФРУ, выбрав разрешение выводных файлов:')
		print('(по умолчанию PNG)')
		print('1 - PNG')
		print('2 - JPG')
		print('3 - JPEG')
		e = str(input(''))
		if e == '2':
			rash = '.jpg'
		elif e == '3':
			rash = '.jpeg'
		else:
			rash = '.png'


		print('Ввод данных завершён')
	else:
		dir_name = desktop + '\\Ввод'
		dir2_name = desktop + '\\Вывод'
		rash = '.png'
	print('Выполнение...')
	## Сам код:
	list1 = []
	list_file = []
	for root, dirs, files in os.walk(dir_name):
		for file in files:
			list1.append(dir_name + '\\' + file)
			list_file.append(file)
	u = 1
	l = len(list1)
	for im_str in list1:
		try:
			try:
				im = Image.open(im_str)
				print('Выполнено ' + str(u) + '/' + str(l) + ' (' + list_file[u-1] +')')
				(width, height) = im.size
				if width <= height:
					wh = width // 5
				else:
					wh = height // 5
				path = my_dir
				if wh <= 108:
					wat_num = 1
				elif wh > 108 and wh <= 145:
					wat_num = 2
				elif wh > 145 and wh <= 160:
					wat_num = 3
				elif wh > 160 and wh <= 255:
					wat_num = 4
				elif wh > 255 and wh <= 355:
					wat_num = 5
				elif wh > 355 and wh <= 460:
					wat_num = 6
				else:
					wat_num = 7
				watermark = Image.open(path + '\\wat' + str(wat_num) + '.png')
				watermark = watermark.transform((wh, wh), Image.EXTENT, [0, 0, watermark.width, watermark.height])
				otstup = wh // 10
				im.paste(watermark.convert('RGB'), (otstup, otstup), watermark)
				im.save(dir2_name + '\\' + str(u) + rash)
			except Exception as E:
				print('Ошибка: ' + str(E))
				print('Не выполнено ' + str(u) + '/' + str(l) + ' (' + list_file[u-1] +')')

		except Exception as E:
			print('Ошибка: ' + str(E))
			print('Не выполнено ' + str(u) + '/' + str(l) + ' (' + list_file[u - 1] + ')')
		u+=1
	print('Готово')
	print('Нажмите Enter, чтобы выйти или введите что угодно, после нажав Enter, чтобы вернуться в начало:')
	t = input('')
	if t != '':
		de()
de()