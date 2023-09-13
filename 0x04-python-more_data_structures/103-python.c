#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *element;
size = PyList_Size(p);
printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, ((PyListObject *)p)->allocated);
for (i = 0; i < size; i++)
{
element = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
if (PyBytes_Check(element))
printf("[.] bytes object info\n  size: %ld\n  trying string: %s\n", PyBytes_Size(element), PyBytes_AsString(element));
}
}
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
