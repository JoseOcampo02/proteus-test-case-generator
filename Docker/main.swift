//
//  main.swift
//  Proteus
//
//  Created by Matthew Fuller on 9/30/21.
//  Copyright © 2022 CSUNTAVLAB. All rights reserved.
//

import ArgumentParser
import Foundation

var errorStream = StandardErrorOutputStream()

struct ProteusCompiler: ParsableCommand {
    static var configuration = CommandConfiguration(
        abstract: "A Proteus language compiler written in Swift.",
        version: "0.0.1",
        subcommands: [Build.self]
    );
}

extension ProteusCompiler {
    struct Build: ParsableCommand {
        static var configuration = CommandConfiguration(
            abstract: """
                Build a `.proteus` file into a valid C language \
                output file that utilizes QPC.
                """)

        @Argument(help: "The input `.proteus` file to build.")
        var inputFile: String

        mutating func run() {
            build(inputFile)
        }
    }
}

private func build(_ inputFile: String) {
//    guard let QPC = ProcessInfo.processInfo.environment["QPC"] else {
//        print(
//            """
//            QPC path needs to be defined as an ENVIRONMENT variable for \
//            swift-proteus to work.
//            """,
//            to: &errorStream
//        )
//        return
//    }

    let inputResult: InputResult
    do {
        inputResult = try readInput(inputFile)
    } catch {
        print("Error info: \(error)", to: &errorStream)
        return
    }

    let inputFileContents: String
    do {
        inputFileContents = try inputResult.get()
    } catch {
        print("Error info: \(error)", to: &errorStream)
        return
    }

    let result: LexerResult = Lexer(input: inputFileContents).lexify()
    var tokens: Array<Sourced<Token>> = Array()
    switch result {
    case .success(let data):
        tokens = data
    case .failure(let data):
        print(data.getWhat(), to: &errorStream)
        return
    }

//    if case let .success(tokens) = result {
//        print(tokens.count)
//        print("The tokens are:\n")
//        var stringTokens = String()
//        for token in tokens[0..<tokens.count - 1] {
//            stringTokens += token.getInner().printDebugToken()
//            stringTokens += " "
//        }
//        stringTokens += tokens.last!.getInner().printDebugToken()
//        stringTokens += "\n"
//
//        print(stringTokens)
//    }

    let parserInput: ParserInput
    do {
        parserInput = try ParserInput(tokens: tokens)
    } catch let error {
        print("Error info: \(error.localizedDescription)", to: &errorStream)
        return
    }

    let parser = Parser(parserInput: parserInput)
    let program: Program
    do {
        program = try parser.parseProgram().get()
    } catch let error {
        print("Parser Error: \(error)", to: &errorStream)
        return
    }

//    switch parser.parseProgram() {
//    case .success(let data):
//        program = data
//    case .failure(let data):
//        print()
//        print("parser failure dump:")
//        print(data.getErrorType())
//        print(data.getLocation().getSourceFirst().line)
//        print(data.getLocation().getSourceSecond().line)
//        print(data.getLocation().getSourceFirst().column)
//        print(data.getLocation().getSourceSecond().column)
//        print(data.getLocation().getSourceFirst().index)
//        print(data.getLocation().getSourceSecond().index)
//        print(data.getWhat())
//        return
//    }

    let typeEnvironment: TypeEnvironment
    do {
        let typechecker = try TypeChecker(program: program)
        switch try typechecker.typecheck() {
        case .success(let data):
            typeEnvironment = data
        case .failure(let data):
            print("typechecker failure dump:")
            print(data.getErrorType())
            print(data.getLocation().getSourceFirst().line)
            print(data.getLocation().getSourceSecond().line)
            print(data.getLocation().getSourceFirst().column)
            print(data.getLocation().getSourceSecond().column)
            print(data.getLocation().getSourceFirst().index)
            print(data.getLocation().getSourceSecond().index)
            print(data.getWhat())
            return
        }
    } catch TypecheckerError.error(let string) {
        print("Typechecker: \(string)", to: &errorStream)
        return
    } catch TypeEnvironmentError.error(let string) {
        print("TypeEnvError: \(string)", to: &errorStream)
        return
    } catch ScopeError.error(let string) {
        print("ScopeError: \(string)", to: &errorStream)
        return
    } catch GenEnvironmentError.error(let string) {
        print("GenEnvError: \(string)", to: &errorStream)
        return
    } catch FuncBuilderError.error(let string) {
        print("FuncBuilderError: \(string)", to: &errorStream)
        return
    } catch BuiltinFunctionError.error(let string) {
        print("BuiltinFunctionError: \(string)", to: &errorStream)
        return
    } catch LValueCheckerError.error(let string) {
        print("LValueCheckerError: \(string)", to: &errorStream)
        return
    } catch let unknownError {
        print("Error: \(unknownError)", to: &errorStream)
        print("Error type: \(unknownError.localizedDescription)", to: &errorStream)
        if let dispStyle = Mirror(reflecting: unknownError).displayStyle {
            print("Error type displaystyle: \(dispStyle)", to: &errorStream)
        }
        return
    }

    print("Success!")
}

ProteusCompiler.main()
