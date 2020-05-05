import os, glob, argparse
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def generate(input_dir, template_glob, output_dir):
    env = Environment(loader=FileSystemLoader(input_dir))
    env.trim_blocks = True
    env.lstrip_blocks = True

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for template_file in list(glob.glob(input_dir +"/"+template_glob)):
        print("Process file '" + template_file +"'...")
        file = os.path.basename(template_file)
        template = env.get_template(file)
        output_from_parsed_template = template.render()
        output_file = os.path.join(output_dir,os.path.splitext(file)[0]+".html")
        with open(output_file, "w", encoding="utf-8") as fh:
            fh.write(output_from_parsed_template)
        print("Output saved to '" + output_file + "'...")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder',default='templates', help="Specify the templates folder.")
    parser.add_argument('-g', '--glob', default='*.j2', help="Specify the file pattern.")
    parser.add_argument('-o', '--output',default='out', help="Specify the output folders.")
    args = parser.parse_args()
    generate(args.folder, args.glob,args.output)

if __name__ == '__main__':
    main()
