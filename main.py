import sys
from programfiles.registermanager import (
    Register_Manager
)
from programfiles.iofunctions import (
    get_parsed_arguments,
    load_register_from_file,
    save_data_to_file,
    get_results_string
)
from programfiles.exceptioninfo import (
    get_exception_info
)


def main(arguments):
    args = get_parsed_arguments(arguments)

    try:
        with open(args.source, 'r') as source_file:
            register = load_register_from_file(source_file)
        manager = Register_Manager(register)
        manager.calculate_outputs(args)
    except Exception as exception:
        print(get_exception_info(exception, args.source))
        return

    if args.save:
        with open(args.save, 'w') as file_handle:
            save_data_to_file(file_handle, manager.outputs)

    if args.show:
        print(get_results_string(manager.outputs))


if __name__ == '__main__':
    main(sys.argv)
