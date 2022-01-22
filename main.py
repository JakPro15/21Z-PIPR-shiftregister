import sys
from programfiles.resultsfunctions import (
    get_sequences,
    get_average_sequence_diversity,
    get_space_usage
)
from programfiles.iofunctions import (
    load_register_from_file,
    save_data_to_file,
    get_parsed_arguments,
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
        sequences = get_sequences(register, args)
    except Exception as exception:
        print(get_exception_info(exception, args.source))
        return

    average_sequence_diversity = round(
        get_average_sequence_diversity(sequences), 4)
    space_usage = round(get_space_usage(sequences), 4)

    if args.save:
        with open(args.save, 'w') as file_handle:
            save_data_to_file(file_handle, sequences, space_usage,
                              average_sequence_diversity)

    if args.show:
        print(get_results_string(sequences, space_usage,
                                 average_sequence_diversity))


if __name__ == '__main__':
    main(sys.argv)
