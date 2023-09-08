from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from main.domain.cv import CV
from main.ports.cv_formatter import CVFormatter

class DOCXCVFormatter(CVFormatter):

    def format(self, cv: CV, output_file: str):
        doc = Document()
        
        # Name
        name_para = doc.add_paragraph()
        run = name_para.add_run(cv.name)
        run.bold = True
        run.font.size = Pt(14)
        name_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # Position
        position_para = doc.add_paragraph()
        run = position_para.add_run(cv.position)
        run.bold = True
        run.font.size = Pt(10)
        position_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # Summary
        summary_para = doc.add_paragraph()
        run = summary_para.add_run('Summary of Qualifications')
        run.bold = True
        summary_para.alignment = WD_ALIGN_PARAGRAPH.LEFT
        doc.add_paragraph(cv.summary).alignment = WD_ALIGN_PARAGRAPH.LEFT

        # Skills
        skills_para = doc.add_paragraph()
        run = skills_para.add_run('Skills')
        run.bold = True
        skills_para.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for skill_category in cv.skills:
            cat_para = doc.add_paragraph()
            run = cat_para.add_run(skill_category.name)
            run.bold = True
            for skill in skill_category.skills:
                doc.add_paragraph(skill)
                
        # Experience
        experience_para = doc.add_paragraph()
        run = experience_para.add_run('Experience')
        run.bold = True
        experience_para.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for project in cv.experience:
            doc.add_paragraph().add_run('Project Name:').bold = True
            doc.add_paragraph(project.name)
            doc.add_paragraph().add_run('Project Description:').bold = True
            doc.add_paragraph(project.description)
            doc.add_paragraph().add_run('Customer:').bold = True
            doc.add_paragraph(project.customer)
            doc.add_paragraph().add_run('Duration:').bold = True
            doc.add_paragraph(project.duration)
            doc.add_paragraph().add_run('Role:').bold = True
            doc.add_paragraph(project.role)
            doc.add_paragraph().add_run('Responsibilities:').bold = True
            doc.add_paragraph(project.responsibilities)
            doc.add_paragraph().add_run('Team Size:').bold = True
            doc.add_paragraph(str(project.team_size))
            doc.add_paragraph().add_run('Tools & Technologies:').bold = True
            doc.add_paragraph(', '.join(project.tools_technologies))
            
        # Save to the specified output file
        doc.save(output_file)

    def get_extension(self):
        return '.docx'
