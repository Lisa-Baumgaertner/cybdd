# this file contains the script for prerpocessing the JSONL-dataset for the fine-tuning process
# code llama instruct 7b

import json

# Datenset laden
with open ("C:\\Users\\Uni\\Desktop\\cy_bdd_final_dataset_multipage_included.jsonl", "r", encoding="utf-8") as file:
    dataset = [json.loads(zeile) for zeile in file]


# Zusammenfügen der verschiedenen Felder aus der JSONL-Datei, 
# Um Format prompt, output zu entsprechen
# Momentan zu viele Felder
# Zu prompt: instruction, html_context und bdd_scenario
# Zu output: cypress_code
# Zusätzlich wird Zeichen für Beginn einer Sequenz <s> und Zeichen für Ende </s> eingefügt
# Ebenso [INST] und [/INST] um Beginn und Ende der instruction zu signalisieren
# Zur Trennung von html und bdd scenario in der instruction, werden # verwendet

to_save = list()

multi_page = list()
flatten_multi_contexts = ""
new_prompt = ""
new_completion = ""

for d in dataset:

    if "html_context" in d:
        # Felder sortieren
        instruction = d["instruction"] # instruction
        html_context = d["html_context"] # instruction
        bdd_scenario = d["bdd_scenario"] # instruction
        cy_code = d["cypress_code"] # output
        style = d["style"] # imperative oder declarative

        # Felder zu neuem Prompt zusammenfügen
        new_prompt = f"<s>[INST] {instruction}\n\n#### Style\n{style}\n\n#### HTML Context\n{html_context}\n\n#### BDD Scenario\n{bdd_scenario} [/INST]"
    
        # Neues Output Feld + Sequenzende signalisieren
        new_completion = cy_code.strip() + " </s>"

        # Zu neuer Liste zusammenfügen
        to_save.append({"prompt": new_prompt, "completion": new_completion})

    elif "multi_page_html_contexts" in d:
        flatten_multi_contexts = ""
        get_details = ""

        counter_temp = 0

        for name in d["multi_page_html_contexts"]:
            #print(name.get('name'))
            #print("Type of `name`:", type(name))
            #print("Value of `name`:", name.get('name'))

            # if isinstance(name, dict):
            #     name_temp = name.get("name", "UNKNOWN")
            #
            #     print(str(counter_temp) + ' in if: ' + name_temp)
            #     counter_temp += 1
            # else:
            #     name_temp = str(name)
            #     print(str(counter_temp) + ' in else: ' + name_temp)
            #     counter_temp += 1
            #name_temp = name.get('name')
            flatten_multi_contexts += "Page title: " + name.get('name') + "\n"
            #print(flatten_multi_contexts)
            for el in name["elements"]:
                #print(el.get("type"))
                element_type = el.get("type", "unknown_element")
                #print(element_type)
                sel_type = el.get("selector_type", "unknown_sel_type")
                sel = el.get("selector", "unknown_sel")
                text = el.get("text", "unknown_label")


                build_string = element_type + " [" + sel_type + "=" + '"' + sel + '"]'

                if text:
                    build_string += " with text " + text 
                    

                flatten_multi_contexts += build_string + '\n'

                if "children" in el:
                    for child in el["children"]:
                        chi_type = child.get("type", "unknown_element")
                        chi_sel_type = child.get("selector_type", "unknown_sel_type")
                        chi_sel = child.get("selector", "unknown_sel")
                        chi_label = child.get("label", "")
                        chi_text = child.get("text", "")

                        build_string = "\t child element: " + chi_type + " [" + chi_sel_type + "=" + '"' + chi_sel + '"]'

                        if chi_text:
                            build_string += " with text " + chi_text

                        flatten_multi_contexts += build_string + '\n'

                        if "children" in child:
                            for dp_child in child["children"]:
                                dpchi_type = dp_child.get("type", "unknown_element")
                                dpchi_sel_type = dp_child.get("selector_type", "unknown_sel_type")
                                dpchi_sel = dp_child.get("selector", "unknown_sel")
                                dpchi_label = dp_child.get("label", "")
                                dpchi_text = dp_child.get("text", "")

                                build_string = "\t child element: " + dpchi_type + " [" + dpchi_sel_type + "=" + '"' + dpchi_sel + '"]'

                                if dpchi_text:
                                    build_string += " with text " + dpchi_text

                                flatten_multi_contexts += build_string + '\n'

        new_prompt = f"<s>[INST] {instruction}\n\n#### Style\n{style}\n\n#### HTML Multi-Page Context\n{flatten_multi_contexts}\n\n#### BDD Scenario\n{bdd_scenario} [/INST]"
        # Neues Output Feld + Sequenzende signalisieren
        new_completion = cy_code.strip() + " </s>"

        

        # Zu neuer Liste zusammenfügen
        to_save.append({"prompt": new_prompt, "completion": new_completion})


# speichern als JSONL wieder
# es muss w+ verwendet werden, falls Datei noch nicht existiert
with open("C:\\Users\\Uni\\Downloads\\dataset_preprocessed.jsonl", "w+", encoding="utf-8") as file:
    for sample in to_save:
        file.write(json.dumps(sample) + "\n")


