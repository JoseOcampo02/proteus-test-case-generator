// swift-tools-version:5.6.2

import PackageDescription

let package = Package(
    name: "Proteus",
    products: [
        .executable(name: "Proteus", targets: ["Proteus"]),
    ],
    dependencies: [
        .package(url: "https://github.com/apple/swift-argument-parser.git", from: "1.0.0"),
    ],
    targets: [
        .target(
            name: "Proteus",
            dependencies: [.product(name: "ArgumentParser", package: "swift-argument-parser")],
            path: "Sources"
        )
    ]
)
