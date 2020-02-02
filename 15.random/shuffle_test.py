import random

list = ["Et",
        "june",
        "Sa",
        "lucas",
        "JJ",
        "LIN"
        ]

list_sub = ["claire",
            "Lyz",
            "fernando",
            "dorosi",
            "lena"
            ]

random.shuffle(list)

for idx, value in enumerate(list):
    print(str(idx + 1) + "조 ", end='')
    print(list[idx + 2 - len(list)] + " 인터뷰조. 인터뷰, 촬영: " + list[idx] + ", 편집:" + list[idx + 1 - len(list)], end='')
    if len(list_sub) > idx:
        print(", 일꾼: " + list_sub[idx])
    else:
        print()
