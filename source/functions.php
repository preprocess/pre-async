<?php

namespace Pre\Async;

use Yay\Ast;

function closure($ast) {
    if (function_exists("\\Amp\\resolve")) {
        $append = new Ast("amp1");
        $append->push(new Ast());
        $ast->append($append);
    } else {
        $append = new Ast("amp2");
        $append->push(new Ast());
        $ast->append($append);
    }

    $defined = [];
    $yields = false;

    foreach ($ast->{"functionArguments"} as $node) {
        $name = $node["functionArgument"]["functionArgumentName"]->value();
        $defined[$name] = true;
    }

    $bound = false;
    $scope = new Ast("scope");

    $pushed = [];

    foreach ($ast->{"body"} as $token) {
        $name = $token->value();

        if (in_array($token->value(), ["yield", "await"])) {
            $yields = true;
            continue;
        }

        if (!$token->is(T_VARIABLE)) {
            continue;
        }

        if (isset($defined[$name]) || isset($pushed[$name])) {
            continue;
        }

        if (substr($name, 1) === "this") {
            continue;
        }

        $pushed[$name] = true;
        $scope->push(new Ast("var", $token));
        $bound = true;
    }

    if ($bound) {
      $ast->append($scope);
    }

    if (!$yields) {
        $append = new Ast("yields");
        $append->push(new Ast());

        $ast->append($append);
    }
}
