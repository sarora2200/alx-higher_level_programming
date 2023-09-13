#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Function prints basic info about Python lists.
 * @p: PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int length, alloc, e;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	length = var->ob_length;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %d\n", alloc);

	for (e = 0; e < length; e++)
	{
		type = list->ob_item[e]->ob_type->tp_name;
		printf("Element %d: %s\n", e, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[e]);
	}
}

/**
 * print_python_bytes - Function prints basic info about Python byte objects.
 * @p: PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char e, length;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_length);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_length > 10)
		length = 10;
	else
		length = ((PyVarObject *)p)->ob_length + 1;

	printf("  first %d bytes: ", length);
	for (e = 0; e < size; e++)
	{
		printf("%02hhx", bytes->ob_sval[e]);
		if (e == (length - 1))
			printf("\n");
		else
			printf(" ");
	}
}
