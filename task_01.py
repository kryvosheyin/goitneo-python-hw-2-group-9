def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No contact found with that name"
        except IndexError:
            return "Give me name please."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: list, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} was added"


@input_error
def change_contact(args: list, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} was updated with {phone}"
    else:
        raise KeyError


@input_error
def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return add_if_not_exists(name, contacts)


@input_error
def add_if_not_exists(name, contacts_list):
    response = (
        input(
            f"{name} is not found in the contacts list. Would you like to add one now? y/n: "
        )
    ).lower()
    if response in ["y", "yes"]:
        phone = input(f"Enter contact information for {name}: ").split()
        return add_contact([name, phone[0]], contacts_list)
    elif response in ["n", "no", "not"]:
        return "As you wish, master"
    else:
        return "I take it as NO"


@input_error
def print_contacts(_, contacts_list):
    all_contacts = "\n{:<15}{}\n\n".format("NAME", "CONTACT INFO")
    for contact, contact_info in contacts_list.items():
        all_contacts += f"{contact:<15}: {contact_info}\n"
    return all_contacts


def print_hello(args, contacts):
    return "How can I help you?"


def valid_arguments(args):
    if len(args) != 2:
        return False
    return True


def main():
    contacts = {}
    COMMANDS = {
        "add": add_contact,
        "update": change_contact,
        "change": change_contact,
        "phone": get_phone,
        "all": print_contacts,
        "hello": print_hello,
    }

    print("Welome to the assistant bot!")
    while True:
        user_input = input("Enter the command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "goodbye"]:
            print("Goodbye!")
            break
        elif command in COMMANDS:
            resut = COMMANDS[command](args, contacts)
            if resut:
                print(resut)
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
