#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Function prints basic info about Python lists.
 * @p: PyObject list object.
 */
void print_python_list(PyObject *p)
{
        int size, alloc, e;
        const char *type;
        PyListObject *list = (PyListObject *)p;
        PyVarObject *var = (PyVarObject *)p;

        size = var->ob_size;
        alloc = list->allocated;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %d\n", size);
        printf("[*] Allocated = %d\n", alloc);

        for (e = 0; e < size; e++)
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
        unsigned char e, size;
        PyBytesObject *bytes = (PyBytesObject *)p;

        printf("[.] bytes object info\n");
        if (strcmp(p->ob_type->tp_name, "bytes") != 0)
        {
                printf("  [ERROR] Invalid Bytes Object\n");
                return;
        }

        printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
        printf("  trying string: %s\n", bytes->ob_sval);

        if (((PyVarObject *)p)->ob_size > 10)
                size = 10;
        else
                size = ((PyVarObject *)p)->ob_size + 1;

        printf("  first %d bytes: ", size);
        for (e = 0; e < size; e++)
        {
                printf("%02hhx", bytes->ob_sval[e]);
                if (e == (size - 1))
                        printf("\n");
                else
                        printf(" ");
        }
}
