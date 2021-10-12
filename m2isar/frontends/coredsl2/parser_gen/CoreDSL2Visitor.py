# Generated from CoreDSL2.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CoreDSL2Parser import CoreDSL2Parser
else:
    from CoreDSL2Parser import CoreDSL2Parser

# This class defines a complete generic visitor for a parse tree produced by CoreDSL2Parser.

class CoreDSL2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by CoreDSL2Parser#description_content.
    def visitDescription_content(self, ctx:CoreDSL2Parser.Description_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#import_file.
    def visitImport_file(self, ctx:CoreDSL2Parser.Import_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#isa.
    def visitIsa(self, ctx:CoreDSL2Parser.IsaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#instruction_set.
    def visitInstruction_set(self, ctx:CoreDSL2Parser.Instruction_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#core_def.
    def visitCore_def(self, ctx:CoreDSL2Parser.Core_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#section.
    def visitSection(self, ctx:CoreDSL2Parser.SectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#section_arch_state.
    def visitSection_arch_state(self, ctx:CoreDSL2Parser.Section_arch_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#section_functions.
    def visitSection_functions(self, ctx:CoreDSL2Parser.Section_functionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#section_instructions.
    def visitSection_instructions(self, ctx:CoreDSL2Parser.Section_instructionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#instruction.
    def visitInstruction(self, ctx:CoreDSL2Parser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#rule_encoding.
    def visitRule_encoding(self, ctx:CoreDSL2Parser.Rule_encodingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#bit_value.
    def visitBit_value(self, ctx:CoreDSL2Parser.Bit_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#bit_field.
    def visitBit_field(self, ctx:CoreDSL2Parser.Bit_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#function_definition.
    def visitFunction_definition(self, ctx:CoreDSL2Parser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#parameter_list.
    def visitParameter_list(self, ctx:CoreDSL2Parser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#parameter_declaration.
    def visitParameter_declaration(self, ctx:CoreDSL2Parser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#statement.
    def visitStatement(self, ctx:CoreDSL2Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#switch_block_statement_group.
    def visitSwitch_block_statement_group(self, ctx:CoreDSL2Parser.Switch_block_statement_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#switch_label.
    def visitSwitch_label(self, ctx:CoreDSL2Parser.Switch_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#block.
    def visitBlock(self, ctx:CoreDSL2Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#block_item.
    def visitBlock_item(self, ctx:CoreDSL2Parser.Block_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#for_condition.
    def visitFor_condition(self, ctx:CoreDSL2Parser.For_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#declaration.
    def visitDeclaration(self, ctx:CoreDSL2Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#declarationSpecifier.
    def visitDeclarationSpecifier(self, ctx:CoreDSL2Parser.DeclarationSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#attribute.
    def visitAttribute(self, ctx:CoreDSL2Parser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#type_specifier.
    def visitType_specifier(self, ctx:CoreDSL2Parser.Type_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#primitive_type.
    def visitPrimitive_type(self, ctx:CoreDSL2Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#bit_size_specifier.
    def visitBit_size_specifier(self, ctx:CoreDSL2Parser.Bit_size_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#enum_type.
    def visitEnum_type(self, ctx:CoreDSL2Parser.Enum_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#enumerator_list.
    def visitEnumerator_list(self, ctx:CoreDSL2Parser.Enumerator_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#enumerator.
    def visitEnumerator(self, ctx:CoreDSL2Parser.EnumeratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#composite_type.
    def visitComposite_type(self, ctx:CoreDSL2Parser.Composite_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#struct_declaration.
    def visitStruct_declaration(self, ctx:CoreDSL2Parser.Struct_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#struct_declaration_specifier.
    def visitStruct_declaration_specifier(self, ctx:CoreDSL2Parser.Struct_declaration_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#init_declarator.
    def visitInit_declarator(self, ctx:CoreDSL2Parser.Init_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#direct_declarator.
    def visitDirect_declarator(self, ctx:CoreDSL2Parser.Direct_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#initializer.
    def visitInitializer(self, ctx:CoreDSL2Parser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#initializerList.
    def visitInitializerList(self, ctx:CoreDSL2Parser.InitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#designated_initializer.
    def visitDesignated_initializer(self, ctx:CoreDSL2Parser.Designated_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#designator.
    def visitDesignator(self, ctx:CoreDSL2Parser.DesignatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#direct_abstract_declarator.
    def visitDirect_abstract_declarator(self, ctx:CoreDSL2Parser.Direct_abstract_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#expression_list.
    def visitExpression_list(self, ctx:CoreDSL2Parser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#cast_expression.
    def visitCast_expression(self, ctx:CoreDSL2Parser.Cast_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#binary_expression.
    def visitBinary_expression(self, ctx:CoreDSL2Parser.Binary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#conditional_expression.
    def visitConditional_expression(self, ctx:CoreDSL2Parser.Conditional_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#deref_expression.
    def visitDeref_expression(self, ctx:CoreDSL2Parser.Deref_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#prefix_expression.
    def visitPrefix_expression(self, ctx:CoreDSL2Parser.Prefix_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#assignment_expression.
    def visitAssignment_expression(self, ctx:CoreDSL2Parser.Assignment_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#postfix_expression.
    def visitPostfix_expression(self, ctx:CoreDSL2Parser.Postfix_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#method_call.
    def visitMethod_call(self, ctx:CoreDSL2Parser.Method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#primary.
    def visitPrimary(self, ctx:CoreDSL2Parser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#slice_expression.
    def visitSlice_expression(self, ctx:CoreDSL2Parser.Slice_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#primary_expression.
    def visitPrimary_expression(self, ctx:CoreDSL2Parser.Primary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#string_literal.
    def visitString_literal(self, ctx:CoreDSL2Parser.String_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#constant.
    def visitConstant(self, ctx:CoreDSL2Parser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#integer_constant.
    def visitInteger_constant(self, ctx:CoreDSL2Parser.Integer_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#floating_constant.
    def visitFloating_constant(self, ctx:CoreDSL2Parser.Floating_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#bool_constant.
    def visitBool_constant(self, ctx:CoreDSL2Parser.Bool_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#character_constant.
    def visitCharacter_constant(self, ctx:CoreDSL2Parser.Character_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#double_left_bracket.
    def visitDouble_left_bracket(self, ctx:CoreDSL2Parser.Double_left_bracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#double_right_bracket.
    def visitDouble_right_bracket(self, ctx:CoreDSL2Parser.Double_right_bracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#data_types.
    def visitData_types(self, ctx:CoreDSL2Parser.Data_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#type_qualifier.
    def visitType_qualifier(self, ctx:CoreDSL2Parser.Type_qualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#storage_class_specifier.
    def visitStorage_class_specifier(self, ctx:CoreDSL2Parser.Storage_class_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#attribute_name.
    def visitAttribute_name(self, ctx:CoreDSL2Parser.Attribute_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoreDSL2Parser#struct_or_union.
    def visitStruct_or_union(self, ctx:CoreDSL2Parser.Struct_or_unionContext):
        return self.visitChildren(ctx)



del CoreDSL2Parser