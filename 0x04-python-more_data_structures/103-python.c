#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - Print information about a Python list object
 * @p: Pointer to a Python object representing a list
 * Description:
 * The print_python_list function provides detailed information about a Python
 * list object.It displays the size of the list, the amount of memory allocated
 * for it,and the types of its elements. If any of the elements in the list are
 * bytes objects, additional information about those objects is also displayed.
 * Parameters:
 * @p: A pointer to a Python object representing a list.
 * Return: None
 */

void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *element;
size = PyList_Size(p);
printf("[*] Python list info\n[*] Size of the Python List
		= %ld\n[*] Allocated = %ld\n", size, ((PyListObject *)p)->allocated);
for (i = 0; i < size; i++)
{
element = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
if (PyBytes_Check(element))
printf("[.] bytes object info\n  size: %ld\n  trying string: %s\n",
		PyBytes_Size(element), PyBytes_AsString(element));
}
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: Pointer to a Python object representing bytes
 * Description:
 * The print_python_bytes function provides detailed information about a Python
 * bytes object. It displays the size of the bytes object, attempts to convert
 * it to a string, and prints the first 10 bytes in hexadecimal format. If the
 * object is not a valid PyBytesObject, an error message is printed.
 * Parameters:
 * @p: A pointer to a Python object representing bytes.
 * Return: None
 */

void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
printf("[.] bytes object info\n");
if (PyBytes_Check(p))
{
size = PyBytes_Size(p);
printf("  size: %ld\n  trying string: %s\n", size, PyBytes_AsString(p));
if (size > 10)
size = 10;
else if (size < 0)
return;
printf("  first %ld bytes: ", size);
for (i = 0; i < size; i++)
{
printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
if (i < size - 1)
printf(" ");
}
}
else
printf("  [ERROR] Invalid Bytes Object\n");
}
