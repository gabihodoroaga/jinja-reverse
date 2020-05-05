import os, re, glob, argparse

def readfile(file_path):
    with open(file_path,"r") as f:
        return f.read()

def generate(template_folder, base_file_name, sample_folder, sample_pattern):

    block_regex = r"(\r\n|\r|\n)([ \t]*)({%\sblock\s([a-zA-Z_]+)\s%}(.*?){% endblock %})"

    base_template = readfile(template_folder+"/"+base_file_name)

    template_pattern = ""
    start = 0
    block_names = []
    for m in re.finditer(block_regex, base_template, flags=re.DOTALL):
        template_pattern+=re.escape(base_template[start:m.span()[0]]) + "(.*?)"
        start = m.span(3)[1]
        block_names.append((m.group(4),m.group(2)))

    template_pattern+=re.escape(base_template[start:])

    for sample_file_name in list(glob.glob(sample_folder +"/"+sample_pattern)):
        sample_file = readfile(sample_file_name)
        output_template = os.path.join(template_folder,os.path.splitext(os.path.basename(sample_file_name))[0]+".j2")
        
        with open(output_template,"w+") as t:
            t.write("{% extends \""+base_file_name+"\" %}")
            for m in re.finditer(template_pattern, sample_file, flags=re.DOTALL):
                for idx, g in enumerate(m.groups()):
                    t.write("\n")
                    t.write("{% block " + block_names[idx][0] + " %}")
                    t.write(g)
                    t.write("\n{% endblock %}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder',default='templates', help="Specify the templates folder.")
    parser.add_argument('-b', '--base',default='base.html', help="Specify the base file.")
    parser.add_argument('-s', '--samples', default='samples', help="Specify the samples folder.")
    parser.add_argument('-g', '--glob',default='*.html', help="Specify the glob pattern.")
    args = parser.parse_args()
    generate(args.folder, args.base,args.samples,args.glob)

if __name__ == '__main__':
    main()
