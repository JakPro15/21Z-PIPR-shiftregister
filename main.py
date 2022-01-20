import sys
from programfiles.resultsfunctions import (
    get_average_sequence_diversity,
    get_space_usage
)
from programfiles.iofunctions import (
    save_data_to_file,
    get_parsed_arguments,
    get_results_string
)
from programfiles.errorcatchers import (
    attempt_to_load_register,
    attempt_to_calculate_sequences
)


def main(arguments):
    args = get_parsed_arguments(arguments)

    register = attempt_to_load_register(args.source)
    if isinstance(register, str):
        print(register)
        return

    sequences = attempt_to_calculate_sequences(register, args)
    if isinstance(sequences, str):
        print(sequences)
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
