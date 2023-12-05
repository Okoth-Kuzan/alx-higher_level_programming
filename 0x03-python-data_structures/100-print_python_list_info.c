#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *obj;
	Py_ssize_t size, i;
	PyObject *item;

	obj = (PyListObject *)p;
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", obj->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

