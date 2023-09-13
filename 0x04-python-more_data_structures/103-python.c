#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Function prints basic info about Python lists.
 * @p: PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int length, allo, e;
	const char *typ;
	Py_List_Object *list = (Py_List_Object *)p;
	Py_Var_Object *var = (Py_Var_Object *)p;

	length = var->ob_size;
	allo = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %d\n", allo);

	for (e = 0; e < length; e++)
	{
		typ = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", e, typ);
		if (strcmp(typ, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Function prints basic info about Python byte objects.
 * @p: vPyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char e, length;
	Py_Bytes_Object *bytes = (Py_Bytes_Object *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((Py_Var_Object *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((Py_Var_Object *)p)->ob_size > 10)
		length = 10;
	else
		length = ((Py_Var_Object *)p)->ob_size + 1;

	printf("  first %d bytes: ", length);
	for (e = 0; e < length; e++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (length - 1))
			printf("\n");
		else
			printf(" ");
	}
}
