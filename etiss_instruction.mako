// ${instr_name}
static InstructionDefinition ${instr_name.lower().replace('.', '_')}_${'_'.join(seen_fields)} (
    ISA${enc_idx}_${core_name},
    "${instr_name.lower()}",
    (uint${enc_idx}_t) ${code_string},
    (uint${enc_idx}_t) ${mask_string},
    [] (BitArray & ba,etiss::CodeSet & cs,InstructionContext & ic)
    {

//-----------
${fields_code}
//-----------

        CodePart & partInit = cs.append(CodePart::INITIALREQUIRED);

        partInit.code() = std::string("//${instr_name}\n");

//-----------
${operation}
//-----------

        % for reg in reg_dependencies:
        partInit.getRegisterDependencies().add(reg_name[${reg}], ${core_default_width});
        % endfor
        % for reg in reg_affected:
        partInit.getAffectedRegisters().add(reg_name[${reg}], ${core_default_width});
        % endfor
        partInit.getAffectedRegisters().add("instructionPointer", 32);

        return true;
    },
    0,
    [] (BitArray & ba, Instruction & instr)
    {
//-----------
${fields_code}
//-----------

        std::stringstream ss;
//-----------
${asm_printer_code}
//-----------
        return ss.str();
    }
);
