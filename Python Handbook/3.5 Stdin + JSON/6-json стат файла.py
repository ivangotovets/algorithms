import json
from dataclasses import dataclass,asdict
from typing import Dict, List


@dataclass
class Message:
    acc: List

    def get_message(self):

        TEMPLATE = {
                    'count': len(acc),
                    'positive_count': len([elem for elem in acc if elem > 0]),
                    'min': min(acc),
                    'max': max(acc),
                    'sum': sum(acc),
                    'average': round((sum(acc) / len(acc)), 2),
        }
        return TEMPLATE


with (
    open('input6.txt', 'r', encoding='UTF-8') as file_in,
    open('output6.json', 'w', encoding='UTF-8') as file_out,
):
    acc = []
    for line in file_in:
        acc += [int(x) for x in line[:-1].split(' ')]

    message = Message(acc)
    out = message.get_message()
    data = json.dumps(out)
    file_out.write(data)

